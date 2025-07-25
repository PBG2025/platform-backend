# main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pdf_utils import extract_text_from_pdf

app = FastAPI()

# Allow frontend (adjust the origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specific domain like ["https://petrobrainglobal.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "FastAPI backend for PBG is running."}

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    contents = await file.read()
    text = extract_text_from_pdf(file.file)
    return {"filename": file.filename, "extracted_text": text[:500]}  # limit preview

