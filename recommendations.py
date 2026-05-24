"""
recommendations.py - Acne Treatment Recommendations
Based on AAD Guidelines of Care for the Management of Acne Vulgaris (2024)
JAAD Article: S0190-9622(23)03389-3

This module provides treatment recommendations structured by 4 severity levels.
"""

RECOMMENDATIONS = {
    "source": "AAD Guidelines of Care for the Management of Acne Vulgaris (2024), JAAD",
    "disclaimer": "ข้อมูลนี้มีจุดประสงค์เพื่อให้คำแนะนำเบื้องต้นเท่านั้น ไม่สามารถใช้ทดแทนการวินิจฉัยและรักษาจากแพทย์ผิวหนังได้ ควรปรึกษาแพทย์ก่อนเริ่มใช้ยาใดๆ",
    "severity_levels": {
        "Mild": {
            "level": 1,
            "label_th": "เล็กน้อย",
            "iga_score": "1-2",
            "description": "สิวอุดตัน (comedones) เล็กน้อย, สิวอักเสบจำนวนน้อย ไม่มีแผลเป็น",
            "description_en": "Few comedones (blackheads/whiteheads) with few inflammatory papules/pustules. No scarring or nodules.",
            "treatment": {
                "topical": [
                    {
                        "name": "Topical Retinoid",
                        "name_th": "ยาทากลุ่ม Retinoid",
                        "examples": "adapalene 0.1%, tretinoin",
                        "usage": "ทาก่อนนอน วันละ 1 ครั้ง",
                        "strength": "strong",
                        "icon": "💊"
                    },
                    {
                        "name": "Benzoyl Peroxide 2.5-5%",
                        "name_th": "เบนโซอิลเปอร์ออกไซด์ 2.5-5%",
                        "examples": "Benzac AC, Panoxyl",
                        "usage": "ทาเช้า วันละ 1 ครั้ง",
                        "strength": "strong",
                        "icon": "🧴"
                    }
                ],
                "oral": [],
                "procedural": []
            },
            "skincare_routine": {
                "morning": [
                    {"step": 1, "action": "ล้างหน้า", "detail": "ใช้ผลิตภัณฑ์ล้างหน้าอ่อนโยน (gentle cleanser)"},
                    {"step": 2, "action": "ทายา", "detail": "Benzoyl Peroxide 2.5-5%"},
                    {"step": 3, "action": "มอยเจอร์ไรเซอร์", "detail": "ใช้มอยเจอร์ไรเซอร์ oil-free, non-comedogenic"},
                    {"step": 4, "action": "กันแดด", "detail": "SPF 30+ ทาทุกวัน (สำคัญมากเมื่อใช้ retinoid)"}
                ],
                "evening": [
                    {"step": 1, "action": "ล้างหน้า", "detail": "ล้างเครื่องสำอางและสิ่งสกปรกออกให้หมด"},
                    {"step": 2, "action": "ทายา", "detail": "Topical Retinoid (adapalene หรือ tretinoin)"},
                    {"step": 3, "action": "มอยเจอร์ไรเซอร์", "detail": "บำรุงผิวเพื่อลดการระคายเคือง"}
                ]
            },
            "precautions": [
                "หลีกเลี่ยงการบีบสิว — เสี่ยงติดเชื้อและเกิดแผลเป็น",
                "Retinoid อาจทำให้ผิวลอกและไวต่อแดด — ต้องทากันแดดทุกวัน",
                "ผลลัพธ์จะเริ่มเห็นชัดหลังใช้ต่อเนื่อง 8-12 สัปดาห์",
                "เริ่มใช้ retinoid วันเว้นวันก่อน แล้วค่อยๆ เพิ่มเป็นทุกวัน"
            ],
            "expected_duration": "8-12 สัปดาห์เห็นผลเบื้องต้น",
            "when_to_see_doctor": "หากใช้ยาทาครบ 12 สัปดาห์แล้วไม่ดีขึ้น หรือสิวเพิ่มขึ้น"
        },

        "Moderate": {
            "level": 2,
            "label_th": "ปานกลาง",
            "iga_score": "3",
            "description": "สิวอักเสบ (papules/pustules) จำนวนปานกลาง อาจมีสิวอุดตันและรอยดำร่วมด้วย",
            "description_en": "Moderate number of inflammatory papules/pustules, possibly with comedones and post-inflammatory hyperpigmentation.",
            "treatment": {
                "topical": [
                    {
                        "name": "Topical Retinoid",
                        "name_th": "ยาทากลุ่ม Retinoid",
                        "examples": "adapalene, tretinoin, tazarotene",
                        "usage": "ทาก่อนนอน",
                        "strength": "strong",
                        "icon": "💊"
                    },
                    {
                        "name": "Benzoyl Peroxide 2.5-5%",
                        "name_th": "เบนโซอิลเปอร์ออกไซด์ 2.5-5%",
                        "examples": "Benzac AC, Panoxyl",
                        "usage": "ทาเช้า",
                        "strength": "strong",
                        "icon": "🧴"
                    },
                    {
                        "name": "Topical Antibiotic + BP",
                        "name_th": "ยาปฏิชีวนะทา + BP",
                        "examples": "Clindamycin 1% + BP (เช่น Duac®)",
                        "usage": "ทาวันละ 1-2 ครั้ง ร่วมกับ BP เสมอ",
                        "strength": "strong",
                        "note": "ห้ามใช้ยาปฏิชีวนะทาเดี่ยว",
                        "icon": "💊"
                    },
                    {
                        "name": "Azelaic Acid 15-20%",
                        "name_th": "อะซีลาอิก แอซิด 15-20%",
                        "examples": "Skinoren, Finacea",
                        "usage": "ทาวันละ 1-2 ครั้ง",
                        "strength": "conditional",
                        "note": "ช่วยลดรอยดำด้วย",
                        "icon": "🧴"
                    }
                ],
                "oral": [
                    {
                        "name": "Oral Doxycycline",
                        "name_th": "ยากิน Doxycycline",
                        "examples": "50-100 mg/วัน",
                        "usage": "กินวันละ 1 ครั้งหลังอาหาร นาน 3-4 เดือนแล้วหยุด",
                        "strength": "strong",
                        "note": "ต้องใช้ร่วมกับ topical BP เสมอ / หลีกเลี่ยงผลิตภัณฑ์นม",
                        "icon": "💊"
                    },
                    {
                        "name": "ยาคุมกำเนิด (COC)",
                        "name_th": "ยาคุมกำเนิดชนิดฮอร์โมนรวม",
                        "examples": "สำหรับผู้หญิง",
                        "usage": "กินทุกวัน",
                        "strength": "conditional",
                        "note": "ช่วยลดสิวจากฮอร์โมน",
                        "icon": "💊"
                    },
                    {
                        "name": "Spironolactone",
                        "name_th": "สไปโรโนแลกโตน",
                        "examples": "50-200 mg สำหรับผู้หญิง",
                        "usage": "กินทุกวัน",
                        "strength": "conditional",
                        "note": "ไม่ต้องเจาะ K+ ในคนสุขภาพดี",
                        "icon": "💊"
                    }
                ],
                "procedural": []
            },
            "skincare_routine": {
                "morning": [
                    {"step": 1, "action": "ล้างหน้า", "detail": "ใช้ผลิตภัณฑ์ล้างหน้าอ่อนโยน"},
                    {"step": 2, "action": "ทายา", "detail": "BP หรือ BP+Clindamycin"},
                    {"step": 3, "action": "มอยเจอร์ไรเซอร์", "detail": "oil-free, non-comedogenic"},
                    {"step": 4, "action": "กันแดด", "detail": "SPF 30+"}
                ],
                "evening": [
                    {"step": 1, "action": "ล้างหน้า", "detail": "ล้างเครื่องสำอางและกันแดดออก"},
                    {"step": 2, "action": "ทายา", "detail": "Topical Retinoid"},
                    {"step": 3, "action": "มอยเจอร์ไรเซอร์", "detail": "บำรุงผิวเพื่อลดอาการแห้งลอก"}
                ]
            },
            "precautions": [
                "ห้ามใช้ยาปฏิชีวนะกินเดี่ยว — ต้องใช้ร่วม BP เสมอเพื่อป้องกันเชื้อดื้อยา",
                "จำกัดระยะเวลาใช้ยาปฏิชีวนะกินไม่เกิน 3-4 เดือน",
                "Doxycycline อาจทำให้ไวต่อแสงแดดมากขึ้น — ทากันแดดทุกวัน",
                "กิน Doxycycline หลังอาหาร พร้อมน้ำเยอะๆ หลีกเลี่ยงผลิตภัณฑ์นม",
                "ไม่ควรนอนทันทีหลังกิน Doxycycline (เสี่ยง esophagitis)"
            ],
            "expected_duration": "8-12 สัปดาห์เห็นผลเบื้องต้น, ยาปฏิชีวนะ 3-4 เดือน",
            "when_to_see_doctor": "หากสิวไม่ดีขึ้นหลังจากใช้ยากิน 3-4 เดือน หรือมีแผลเป็นเกิดขึ้น"
        },

        "Severe": {
            "level": 3,
            "label_th": "รุนแรง",
            "iga_score": "4",
            "description": "สิวอักเสบจำนวนมาก มี nodules เริ่มเกิดแผลเป็น ส่งผลกระทบต่อจิตใจ",
            "description_en": "Many inflammatory lesions, nodules present, early scarring, significant psychosocial impact.",
            "treatment": {
                "topical": [
                    {
                        "name": "Topical Retinoid",
                        "name_th": "ยาทากลุ่ม Retinoid",
                        "examples": "adapalene, tretinoin, tazarotene",
                        "usage": "ทาก่อนนอน",
                        "strength": "strong",
                        "icon": "💊"
                    },
                    {
                        "name": "Benzoyl Peroxide 5-10%",
                        "name_th": "เบนโซอิลเปอร์ออกไซด์ 5-10%",
                        "examples": "Benzac AC, Panoxyl",
                        "usage": "ทาเช้า",
                        "strength": "strong",
                        "icon": "🧴"
                    }
                ],
                "oral": [
                    {
                        "name": "Oral Doxycycline",
                        "name_th": "ยากิน Doxycycline",
                        "examples": "100 mg/วัน",
                        "usage": "กินวันละ 1-2 ครั้ง นาน 3-4 เดือน",
                        "strength": "strong",
                        "icon": "💊"
                    },
                    {
                        "name": "Oral Isotretinoin",
                        "name_th": "ยากิน Isotretinoin (ไอโซเตรติโนอิน)",
                        "examples": "0.5-1 mg/kg/วัน",
                        "usage": "กินทุกวันพร้อมอาหารที่มีไขมัน",
                        "strength": "strong",
                        "note": "แนะนำอย่างยิ่งหากไม่ตอบสนองต่อยาทา+ยากินปฏิชีวนะ หรือมีแผลเป็น",
                        "icon": "⚠️"
                    }
                ],
                "procedural": [
                    {
                        "name": "Intralesional Corticosteroid",
                        "name_th": "ฉีดคอร์ติโคสเตียรอยด์เข้ารอยโรค",
                        "usage": "สำหรับ nodule ที่ปวดมาก — ช่วยลดอักเสบเร็ว",
                        "strength": "good_practice",
                        "icon": "💉"
                    }
                ]
            },
            "skincare_routine": {
                "morning": [
                    {"step": 1, "action": "ล้างหน้า", "detail": "ใช้ผลิตภัณฑ์ล้างหน้าอ่อนโยนมาก"},
                    {"step": 2, "action": "ทายา", "detail": "BP (ถ้าไม่ได้ใช้ isotretinoin)"},
                    {"step": 3, "action": "มอยเจอร์ไรเซอร์", "detail": "มอยเจอร์ไรเซอร์เข้มข้น เพราะผิวอาจแห้งมากจากยา"},
                    {"step": 4, "action": "กันแดด", "detail": "SPF 50+ (สำคัญมาก)"}
                ],
                "evening": [
                    {"step": 1, "action": "ล้างหน้า", "detail": "ล้างหน้าอ่อนโยน"},
                    {"step": 2, "action": "ทายา", "detail": "Retinoid หรือตามแพทย์สั่ง"},
                    {"step": 3, "action": "มอยเจอร์ไรเซอร์", "detail": "มอยเจอร์ไรเซอร์เข้มข้น + ลิปบาล์ม"}
                ]
            },
            "precautions": [
                "⚠️ Isotretinoin: ห้ามตั้งครรภ์อย่างเด็ดขาด (teratogenic) — ต้องคุมกำเนิดอย่างเข้มงวด",
                "ผิวแห้งมากจาก Isotretinoin — ต้องใช้มอยเจอร์ไรเซอร์และลิปบาล์มเป็นประจำ",
                "ต้องตรวจเลือดตามแพทย์แนะนำ",
                "Isotretinoin กินพร้อมอาหารที่มีไขมันเพื่อเพิ่มการดูดซึม",
                "ปรึกษาแพทย์ผิวหนังเสมอก่อนเริ่ม Isotretinoin"
            ],
            "expected_duration": "Isotretinoin: 4-6 เดือน / แนวทางอื่น: 3-4 เดือนแล้วประเมินซ้ำ",
            "when_to_see_doctor": "ควรพบแพทย์ผิวหนังเพื่อประเมินและเริ่มยาที่เหมาะสม"
        },

        "Very Severe": {
            "level": 4,
            "label_th": "รุนแรงมาก",
            "iga_score": "4+",
            "description": "สิวถุง (cystic/nodulocystic) ทั่วใบหน้า แผลเป็นเกิดขึ้นเร็ว อาจลามไปลำตัว ส่งผลกระทบต่อคุณภาพชีวิตอย่างมาก",
            "description_en": "Widespread cystic/nodulocystic acne, rapid scarring, possibly extending to trunk. Major quality of life impact.",
            "treatment": {
                "topical": [
                    {
                        "name": "Gentle Cleanser + Heavy Moisturizer",
                        "name_th": "ล้างหน้าอ่อนโยน + มอยเจอร์ไรเซอร์เข้มข้น",
                        "examples": "Cetaphil, CeraVe",
                        "usage": "เช้าและเย็น — เน้นดูแลผิวระหว่างใช้ Isotretinoin",
                        "strength": "good_practice",
                        "icon": "🧴"
                    }
                ],
                "oral": [
                    {
                        "name": "Oral Isotretinoin",
                        "name_th": "ยากิน Isotretinoin (ไอโซเตรติโนอิน)",
                        "examples": "0.5-1 mg/kg/วัน (cumulative dose 120-150 mg/kg)",
                        "usage": "กินทุกวันพร้อมอาหารไขมัน นาน 4-6 เดือน",
                        "strength": "strong",
                        "note": "First-line สำหรับระดับนี้",
                        "icon": "⚠️"
                    },
                    {
                        "name": "Oral Prednisone (short course)",
                        "name_th": "ยากิน Prednisone ระยะสั้น",
                        "examples": "เฉพาะกรณี acne fulminans",
                        "usage": "กินระยะสั้นก่อนเริ่ม Isotretinoin",
                        "strength": "conditional",
                        "note": "ใช้เฉพาะกรณีอักเสบรุนแรงมาก",
                        "icon": "💊"
                    }
                ],
                "procedural": [
                    {
                        "name": "Intralesional Corticosteroid",
                        "name_th": "ฉีดคอร์ติโคสเตียรอยด์เข้ารอยโรค",
                        "usage": "สำหรับ cyst/nodule ที่ปวดมาก",
                        "strength": "good_practice",
                        "icon": "💉"
                    }
                ]
            },
            "skincare_routine": {
                "morning": [
                    {"step": 1, "action": "ล้างหน้า", "detail": "ล้างหน้าอ่อนโยนมาก ไม่มี active ingredients"},
                    {"step": 2, "action": "มอยเจอร์ไรเซอร์", "detail": "มอยเจอร์ไรเซอร์เข้มข้น (ceramide-based)"},
                    {"step": 3, "action": "กันแดด", "detail": "SPF 50+ ทาทุกวัน"}
                ],
                "evening": [
                    {"step": 1, "action": "ล้างหน้า", "detail": "ล้างหน้าอ่อนโยนมาก"},
                    {"step": 2, "action": "มอยเจอร์ไรเซอร์", "detail": "มอยเจอร์ไรเซอร์เข้มข้น + ลิปบาล์ม"},
                    {"step": 3, "action": "ดูแลเพิ่มเติม", "detail": "น้ำตาเทียมหากตาแห้ง, ดื่มน้ำมากๆ"}
                ]
            },
            "precautions": [
                "🚨 ห้ามตั้งครรภ์อย่างเด็ดขาด — ต้องคุมกำเนิดอย่างเข้มงวด",
                "🚨 ห้ามบริจาคเลือดระหว่างใช้ยาและหลังหยุดยา 1 เดือน",
                "⚠️ ห้ามทำ laser/หัตถการผิวหนังระหว่างใช้ยา (ผิวบางและฟื้นตัวช้า)",
                "⚠️ ติดตามอาการทางจิตใจ (mood changes) อย่างใกล้ชิด",
                "ผลข้างเคียง: ผิวแห้ง, ริมฝีปากแตก, ตาแห้ง, ปวดกล้ามเนื้อ",
                "ต้องพบแพทย์ผิวหนังเป็นประจำ"
            ],
            "expected_duration": "Isotretinoin 4-6 เดือน (อาจต้อง course ที่ 2)",
            "when_to_see_doctor": "ต้องพบแพทย์ผิวหนังทันที — ระดับนี้ต้องได้รับการรักษาจากแพทย์โดยตรง"
        }
    },
    "general_good_practices": [
        {"text": "ใช้ยาร่วมกัน (combination therapy) ดีกว่ายาเดี่ยว", "icon": "✅"},
        {"text": "จำกัดการใช้ยาปฏิชีวนะเพื่อป้องกันเชื้อดื้อยา", "icon": "✅"},
        {"text": "ใช้ Benzoyl Peroxide ร่วมกับยาปฏิชีวนะเสมอ", "icon": "✅"},
        {"text": "ฉีด Intralesional corticosteroid สำหรับสิวก้อนใหญ่ที่ปวด", "icon": "✅"},
        {"text": "ประเมินซ้ำด้วย IGA scale (0-4) เพื่อติดตามผล", "icon": "✅"}
    ]
}


# Mapping from class name to key
SEVERITY_MAP = {
    "Mild": "Mild",
    "Moderate": "Moderate",
    "Severe": "Severe",
    "Very Severe": "Very Severe",
}

# Mapping from level number to key
LEVEL_MAP = {
    1: "Mild",
    2: "Moderate",
    3: "Severe",
    4: "Very Severe",
}


def get_recommendation(severity_level: int) -> dict:
    """Get recommendation for a given severity level (1-4)"""
    key = LEVEL_MAP.get(severity_level)
    if not key:
        return {"error": f"Invalid severity level: {severity_level}. Must be 1-4."}

    severity_data = RECOMMENDATIONS["severity_levels"][key]
    return {
        "severity": severity_data,
        "general_good_practices": RECOMMENDATIONS["general_good_practices"],
        "source": RECOMMENDATIONS["source"],
        "disclaimer": RECOMMENDATIONS["disclaimer"],
    }


def get_all_recommendations() -> dict:
    """Get all recommendations data"""
    return RECOMMENDATIONS
