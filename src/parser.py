# src/parser.py
import PyPDF2
from docx import Document

def extract_text(file_path):
    """Extract text from PDF or DOCX file."""
    text = ""
    if file_path.lower().endswith(".pdf"):
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    elif file_path.lower().endswith(".docx"):
        doc = Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
    else:
        raise ValueError(f"Unsupported file type: {file_path}")
    return text

def clean_text(text):
    """Basic text cleaning: remove line breaks, extra spaces, lowercase."""
    return text.replace("\n", " ").strip().lower()
