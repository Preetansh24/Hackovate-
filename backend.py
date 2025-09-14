from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Allow frontend (HTML+JS) to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Models (Input Schemas) ----------
class MilkInput(BaseModel):
    feed_kg: float
    temp_c: float
    humidity: float
    milking_time: float

class DiseaseInput(BaseModel):
    cow_id: str
    day: int
    months_after_birth: int
    previous_mastitis: int
    temperature: float
    breed: str

# ---------- Routes ----------
@app.post("/predict_milk")
def predict_milk(data: MilkInput):
    # Dummy logic
    predicted_yield = (data.feed_kg * 2) - (data.temp_c * 0.1)
    confidence = 0.85
    return {"predicted_yield": predicted_yield, "confidence": confidence}

@app.post("/predict_disease")
def predict_disease(data: DiseaseInput):
    # Dummy disease logic
    if data.temperature > 39:
        return {"disease": "Mastitis", "confidence": 0.92}
    else:
        return {"disease": "Healthy", "confidence": 0.95}
