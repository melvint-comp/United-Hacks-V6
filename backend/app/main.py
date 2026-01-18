from fastapi import FastAPI
from app.api.analyze import router as analyze_router

app = FastAPI(
    title = "Resonance API",
    description = "Chat-Based Interaction Analysis Prototype",
    version = "0.1.0"
)

app.include_router(analyze_router, prefix="/analyze")

@app.get("/")
def root():
    return {
        "message": "Resonance API is running",
        "scope": "Chat-only interaction analysis (tone, empathy, balance)"
    }
