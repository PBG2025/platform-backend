from sqlalchemy import Column, Integer, String
from .database import Base

class PDFUpload(Base):
    __tablename__ = "pdf_uploads"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    url = Column(String)

