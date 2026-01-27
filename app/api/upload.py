from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import uuid
import shutil
from app.db.connection import get_connection
from app.services.ai.company_extractor import extract_company_metadata

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/")
def upload(file: UploadFile = File(...)):
    if not file.filename.lower().endswith((".xlsx", ".xls", ".pdf")):
        raise HTTPException(status_code=400, detail="Only Excel and PDF files are allowed")

    file_id = str(uuid.uuid4())
    stored_name = f"{file_id}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, stored_name)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File save failed: {e}")

    # Store metadata in DB
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO uploaded_files (file_id, original_filename, stored_path)
        VALUES (%s, %s, %s)
        """,
        (file_id, file.filename, file_path)
    )

    conn.commit()

    # Extract company metadata
    company_metadata = extract_company_metadata(file_path)

    # close the db connection
    cursor.close()
    conn.close()

    return {
        "file_id": file_id,
        "status": "uploaded",
        "company_metadata": company_metadata
    }

### two things -- 1. Extract company metadata after file upload -- if company name/id exists then dont add else get company id
# -- salesforce 

### 2. using the company id, add finanancial data into another table. 