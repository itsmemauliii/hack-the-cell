from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np

app = FastAPI(title="Hack the Cell API")

# Request model
class SampleData(BaseModel):
    sample_id: str
    fluorescence: float
    growth: float

@app.get("/")
def root():
    return {"message": "Hack the Cell API is running"}

@app.post("/analyze")
def analyze(data: SampleData):
    # Simple Hill equation model parameters (dummy values)
    F_min, F_max, K_d, n = 100, 1000, 0.5, 2.0
    metal_conc = ((data.fluorescence - F_min) * (K_d ** n) /
                  ((F_max - data.fluorescence) ** (1/n)))
    
    return {
        "sample_id": data.sample_id,
        "estimated_metal_concentration": round(abs(metal_conc), 4),
        "status": "Safe" if metal_conc < 0.3 else "Unsafe"
    }
