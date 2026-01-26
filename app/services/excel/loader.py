import os
import pandas as pd
from typing import Dict
from app.db.connection import get_connection


def load_excel_by_file_id(file_id: str) -> Dict[str, pd.DataFrame]:
    """
    Load all sheets from an uploaded Excel file using file_id.
    """

    # 1. Get file path from DB
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT stored_path FROM uploaded_files WHERE file_id = %s",
        (file_id,)
    )
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if not row:
        raise ValueError(f"No file found for file_id={file_id}")

    file_path = row["stored_path"]

    # 2. Validate file exists
    if not os.path.exists(file_path):
        raise ValueError(f"File not found on disk: {file_path}")

    # 3. Load Excel
    try:
        excel = pd.ExcelFile(file_path)
    except Exception as e:
        raise ValueError(f"Failed to open Excel file: {e}")

    # 4. Load all sheets
    sheets = {}
    for sheet_name in excel.sheet_names:
        try:
            df = excel.parse(sheet_name=sheet_name, header=None)
            sheets[sheet_name] = df
        except Exception as e:
            raise ValueError(f"Failed to parse sheet '{sheet_name}': {e}")

    if not sheets:
        raise ValueError("Excel file contains no readable sheets")

    return sheets
