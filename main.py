from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
import onnxruntime as ort
import numpy as np
import os

app = FastAPI(title="AcneAI Backend", version="1.0.0")

# Allow CORS - restrict to known origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
MODEL_PATH = "model.onnx"
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_TYPES = {"image/jpeg", "image/png", "image/webp"}

# Global model variable
model = None

def load_model():
    global model
    if not os.path.exists(MODEL_PATH):
        print(f"[{MODEL_PATH}] not found. Waiting for file to be placed...")
        return None

    try:
        print(f"Loading ONNX model from {MODEL_PATH}...")
        model = ort.InferenceSession(MODEL_PATH)
        print("Model loaded successfully!")
    except Exception as e:
        print(f"Error loading model: {e}")
        model = None

# Initial load
load_model()

def preprocess_image(image: Image.Image) -> np.ndarray:
    """Preprocess image to match torchvision ToTensor() and Resize()"""
    image = image.resize((640, 640))
    img_array = np.array(image, dtype=np.float32) / 255.0
    img_array = np.transpose(img_array, (2, 0, 1))
    input_tensor = np.expand_dims(img_array, axis=0)
    return input_tensor

# Class name mapping
CLASS_NAMES = ["Mild", "Moderate", "Severe", "Very Severe"]


async def validate_image(file: UploadFile) -> bytes:
    """Validate uploaded file is an image within size limits"""
    # Check content type
    if file.content_type and file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type: {file.content_type}. Allowed: {', '.join(ALLOWED_TYPES)}"
        )

    # Read and check size
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"File too large. Max size: {MAX_FILE_SIZE // (1024*1024)}MB"
        )

    # Verify it's a valid image
    try:
        Image.open(io.BytesIO(contents)).verify()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image file")

    return contents


async def process_single_image(contents: bytes, image_label: str):
    """Process a single image and return predictions"""
    try:
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        input_tensor = preprocess_image(image)

        input_name = model.get_inputs()[0].name
        output = model.run(None, {input_name: input_tensor})[0]

        predictions = []

        # Apply softmax
        exp_out = np.exp(output - np.max(output, axis=1, keepdims=True))
        probs = exp_out / np.sum(exp_out, axis=1, keepdims=True)
        probs = probs[0]

        # Get top 3 predictions
        topk_indices = np.argsort(probs)[::-1][:min(3, len(probs))]

        for idx in topk_indices:
            score = probs[idx]
            name = CLASS_NAMES[idx] if idx < len(CLASS_NAMES) else f"class_{idx}"

            predictions.append({
                "class": name,
                "confidence": round(float(score), 4),
                "source": image_label
            })

        return predictions
    except Exception as e:
        print(f"Error processing {image_label}: {e}")
        return []


def get_mock_predictions(sources=None):
    """Return mock data when model is not loaded"""
    if sources is None:
        sources = ["front"]
    mock = []
    for src in sources:
        mock.append({"class": "mock_inflamed", "confidence": 0.99, "source": src})
    return mock


@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    global model

    # Reload if not loaded
    if model is None:
        load_model()
        if model is None:
            return {
                "predictions": get_mock_predictions(),
                "warning": "Model not loaded. Using mock data. Check server console."
            }

    contents = await validate_image(file)

    try:
        predictions = await process_single_image(contents, "front")
        return {"predictions": predictions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/analyze-multi")
async def analyze_multi_images(
    front: UploadFile = File(...),
    left: UploadFile = File(None),
    right: UploadFile = File(None)
):
    """Analyze multiple face images (front, left, right) and combine results"""
    global model

    # Reload if not loaded
    if model is None:
        load_model()
        if model is None:
            sources = ["front"]
            if left:
                sources.append("left")
            if right:
                sources.append("right")
            return {
                "predictions": get_mock_predictions(sources),
                "images_processed": len(sources),
                "warning": "Model not loaded. Using mock data."
            }

    all_predictions = []
    images_processed = 0

    # Process front image (required)
    if front:
        contents = await validate_image(front)
        preds = await process_single_image(contents, "front")
        all_predictions.extend(preds)
        images_processed += 1

    # Process left image (optional)
    if left:
        contents = await validate_image(left)
        preds = await process_single_image(contents, "left")
        all_predictions.extend(preds)
        images_processed += 1

    # Process right image (optional)
    if right:
        contents = await validate_image(right)
        preds = await process_single_image(contents, "right")
        all_predictions.extend(preds)
        images_processed += 1

    return {
        "predictions": all_predictions,
        "images_processed": images_processed
    }


@app.get("/")
def read_root():
    return {
        "status": "AcneAI Backend Running (ONNX)",
        "model_loaded": model is not None,
    }


@app.get("/health")
def health_check():
    return {
        "healthy": True,
        "model_loaded": model is not None,
    }
