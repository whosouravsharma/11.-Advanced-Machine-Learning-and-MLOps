from app.services.parsers.excel_parser import parse_excel
from app.services.parsers.pdf_parser import parse_pdf

def parse_document(file_path: str) -> dict:
    if file_path.lower().endswith((".xlsx", ".xls")):
        return parse_excel(file_path)
    elif file_path.lower().endswith(".pdf"):
        return parse_pdf(file_path)
    else:
        raise ValueError("Unsupported file type")
