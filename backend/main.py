import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="ComplianceGPT Backend",
    description="AI-powered compliance co-pilot for CA firms",
    version="0.1.0"
)


@app.get("/health")
def health_check():
    """
    Basic health check endpoint.
    Frontend calls this to confirm backend is reachable.
    """
    groq_key_loaded = bool(os.getenv("GROQ_API_KEY"))
    return {
        "status": "ok",
        "groq_key_loaded": groq_key_loaded,
        "message": "ComplianceGPT backend is running."
    }


# ── Future routes will be added here as the project grows ──
# from api.routes import router
# app.include_router(router)
