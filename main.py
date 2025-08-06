import logging
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.api_v1 import api_router

# Enhanced logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info("🚀 FastAPI backend starting...")

# Get environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
PORT = int(os.getenv("PORT", 8080))

# Validate environment variables
if not DATABASE_URL:
    logger.error("DATABASE_URL is not set!")
    raise ValueError("DATABASE_URL environment variable is required")

if not SECRET_KEY:
    logger.error("SECRET_KEY is not set!")
    raise ValueError("SECRET_KEY environment variable is required")

logger.info(f"Using PORT: {PORT}")
logger.info("Environment variables loaded successfully")

app = FastAPI(title="PetrobainGlobal API", version="1.0.0")

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://www.petrobrainglobal.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

# Include routes
app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "PetrobainGlobal API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": "2025-08-06"}

@app.on_event("startup")
async def startup_event():
    logger.info("Application startup complete")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutting down")
