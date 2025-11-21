import json
from pypdf import PdfReader

PDF_PATH = "uk_act.pdf"
OUTPUT_PATH = "extracted.json"

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    extracted_text = ""

    for page in reader.pages:
        text = page.extract_text() or ""
        extracted_text += text + "\n"

    return extracted_text


if __name__ == "__main__":
    text = extract_text_from_pdf(PDF_PATH)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump({"text": text}, f, indent=4)

    print(f"✔ Extracted text saved to {OUTPUT_PATH}")
