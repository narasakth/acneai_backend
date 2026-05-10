FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies with extra index URL to ensure we get the CPU version of PyTorch
# This is crucial for keeping the Docker image size small
RUN pip install --no-cache-dir -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

# Copy the rest of the application code, including model.pth
COPY . .

# Command to run the application
# Google Cloud Run provides the PORT environment variable (default 8080)
CMD exec uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}
