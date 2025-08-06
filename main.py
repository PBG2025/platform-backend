# main.py
import logging
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.api_v1 import api_router

# Log startup
logging.basicConfig(level=logging.INFO)
logging.info("🚀 FastAPI backend starting...")

# Get environment variables from DigitalOcean App Platform
DATABASE_URL = os.getenv("DATABASE_URL","postgresql://default:pass@localhost/dbname")
SECRET_KEY = os.getenv("SECRET_KEY","defaultsecret")

# Optional: log or validate
if not DATABASE_URL:
    logging.error("DATABASE_URL is not set!")
if not SECRET_KEY:
    logging.error("SECRET_KEY is not set!")

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://www.petrobrainglobal.com"],  # Replace with actual frontend domain
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

# Include all routes
app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

