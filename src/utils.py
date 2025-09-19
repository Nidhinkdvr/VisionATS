import os

def list_files(folder_path, extensions=[".pdf", ".docx"]):
    """
    List files in a folder filtered by extensions.
    """
    files = []
    for f in os.listdir(folder_path):
        if any(f.lower().endswith(ext) for ext in extensions):
            files.append(f)
    return files
