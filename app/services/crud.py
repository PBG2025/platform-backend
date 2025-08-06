# crud.py

from sqlalchemy.orm import Session
from models import PDFUpload

# Create a new PDF upload record
def create_pdf_upload(db: Session, filename: str, url: str):
    pdf = PDFUpload(filename=filename, url=url)
    db.add(pdf)
    db.commit()
    db.refresh(pdf)
    return pdf

# Get a PDF by ID
def get_pdf_by_id(db: Session, pdf_id: int):
    return db.query(PDFUpload).filter(PDFUpload.id == pdf_id).first()

# Get all PDFs
def get_all_pdfs(db: Session):
    return db.query(PDFUpload).all()


