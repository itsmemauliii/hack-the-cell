from fastapi import FastAPI
from pydantic import BaseModel
import math

app = FastAPI()

class Sample(BaseModel):
    sample_id: str
    fluorescence: float
    growth: float

@app.post("/analyze")
def analyze(sample: Sample):
    # Example Hill equation parameters
    F_min, F_max, K_d, n = 100, 1000, 0.5, 2.0

    try:
        # Calculate estimated concentration
        conc = ((sample.fluorescence - F_min) * (K_d ** n) /
                ((F_max - sample.fluorescence) ** (1/n)))
        conc = abs(conc)

        status = "Safe" if conc < 0.3 else "Unsafe"
        return {
            "sample_id": sample.sample_id,
            "estimated_metal_concentration": round(conc, 4),
            "status": status
        }
    except Exception as e:
        return {"error": str(e)}
