from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import uuid
import shutil

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True) 


@router.post("/excel")
def upload_excel(file: UploadFile = File(...)):
    if not file.filename.endswith((".xlsx", ".xls")):
        raise HTTPException(status_code=400, detail="Only Excel files are allowed")

    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}_{file.filename}")

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload failed: {e}")

    return {
        "file_id": file_id,
        "file_path": file_path,
        "status": "uploaded"
    }
