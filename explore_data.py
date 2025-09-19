import os
import PyPDF2

# Paths to your data folders
resumes_path = "data/sample_resumes"
jds_path = "data/sample_jds"

# Function to extract text from PDF
def read_pdf(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# Function to process a folder
def explore_folder(folder_path, file_type="Resume"):
    print(f"\n--- {file_type}s in {folder_path} ---")
    for file_name in os.listdir(folder_path):
        if not file_name.lower().endswith(".pdf"):
            print(f"Skipped {file_name} (not PDF)")
            continue
        file_path = os.path.join(folder_path, file_name)
        try:
            text = read_pdf(file_path)
            print(f"\nFile: {file_name}")
            print("Preview (first 500 chars):")
            print(text[:500])
        except Exception as e:
            print(f"Error reading {file_name}: {e}")

# Explore resumes
explore_folder(resumes_path, "Resume")

# Explore job descriptions
explore_folder(jds_path, "Job Description")
