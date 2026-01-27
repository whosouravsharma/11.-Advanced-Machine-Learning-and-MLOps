import pandas as pd

def parse_excel(file_path: str) -> dict:
    xls = pd.read_excel(file_path, sheet_name=None)

    text_blocks = []
    tables = []

    for sheet_name, df in xls.items():
        # Convert entire sheet to text (rough but useful)
        text_repr = df.astype(str).fillna("").to_string(index=False)

        text_blocks.append({
            "location": f"sheet: {sheet_name}",
            "text": text_repr
        })

        # Structured table
        tables.append({
            "location": f"sheet: {sheet_name}",
            "headers": list(df.columns),
            "rows": df.fillna("").values.tolist()
        })

    return {
        "source_type": "excel",
        "text_blocks": text_blocks,
        "tables": tables
    }
