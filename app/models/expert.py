from sqlalchemy import Column, Integer, String
from app.models.base import Base

class Expert(Base):
    __tablename__ = "experts"
    id = Column(Integer, primary_key=True, index=True)
    specialty = Column(String)
    experience_years = Column(Integer)
