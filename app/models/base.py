# app/models/base.py
from app.database import Base

# Re-export Base so other models can import it from here
# This keeps the import structure clean
__all__ = ["Base"]
