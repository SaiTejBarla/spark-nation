from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil

router = APIRouter(tags=["File / Video Uploads"])

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("/uploads/file", summary="Upload a file or video")
async def upload_file(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "status": "Uploaded successfully"}
