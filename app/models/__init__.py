# app/models/__init__.py
from .base import Base
from .user import User  # if you have a User model
from .expert import Expert  # if you have an Expert model
from .upload import PDFUpload

__all__ = ["Base", "User", "Expert", "PDFUpload"]
