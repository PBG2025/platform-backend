# main.py
from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import engine, SessionLocal
import models
import crud
from pdf_utils import extract_text_from_pdf

# Initialize FastAPI
app = FastAPI()

# Allow frontend (adjust the origin as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with actual frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create DB tables on startup
@app.on_event("startup")
def startup_event():
    models.Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Health check
@app.get("/")
def read_root():
    return {"message": "FastAPI backend for PBG is running and connected to DB."}

# Upload endpoint – now stores metadata in DB
@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    text = extract_text_from_pdf(file.file)
    
    # Save upload info to DB (replace URL with actual if you store files)
    saved_pdf = crud.create_pdf_upload(
        db=db,
        filename=file.filename,
        url=f"/uploads/{file.filename}"  # adjust if you're storing files
    )

    return {
        "id": saved_pdf.id,
        "filename": saved_pdf.filename,
        "extracted_text": text[:500]  # preview
    }

