from app.services.parsers.document_parser import parse_document

def extract_company_metadata(file_path: str) -> dict:
    """
    High-level company metadata extraction pipeline.
    """

    # 1. Parse document (PDF / Excel)
    parsed_doc = parse_document(file_path)

    # 2. Inspect parsed output (for now, just return it)
    # Later:
    #   → retrieve relevant chunks (RAG)
    #   → call OpenAI
    #   → normalize output

    print ("Parsed Document Preview:")
    print(parsed_doc)

    return {
        "parsed_preview": {
            "source_type": parsed_doc["source_type"],
            "text_blocks_count": len(parsed_doc["text_blocks"]),
            "tables_count": len(parsed_doc["tables"])
        }
    }
