# app/routes/upload.py
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.utils.pdf_utils import extract_text_from_pdf
from app.services.crud import create_pdf_upload

router = APIRouter()

@router.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    text = extract_text_from_pdf(file.file)
    saved_pdf = create_pdf_upload(db=db, filename=file.filename, url=f"/uploads/{file.filename}")
    return {
        "id": saved_pdf.id,
        "filename": saved_pdf.filename,
        "extracted_text": text[:500]
    }

