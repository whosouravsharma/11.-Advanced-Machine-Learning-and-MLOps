import pdfplumber

def parse_pdf(file_path: str) -> dict:
    text_blocks = []
    tables = []

    with pdfplumber.open(file_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if text:
                text_blocks.append({
                    "location": f"page {page_num}",
                    "text": text
                })

            page_tables = page.extract_tables()
            for table in page_tables:
                headers = table[0]
                rows = table[1:]

                tables.append({
                    "location": f"page {page_num}",
                    "headers": headers,
                    "rows": rows
                })

    return {
        "source_type": "pdf",
        "text_blocks": text_blocks,
        "tables": tables
    }
