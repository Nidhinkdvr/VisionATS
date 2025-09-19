import streamlit as st
import sys
import os

# Add project root so src modules are accessible
sys.path.append("..")

from src import parser, matcher

st.set_page_config(page_title="Resume-JD Matcher", layout="wide")
st.title("AI Resume vs Job Description Matcher")

st.sidebar.header("Upload Files")
resume_file = st.sidebar.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
jd_file = st.sidebar.file_uploader("Upload Job Description (PDF/DOCX)", type=["pdf", "docx"])

if resume_file and jd_file:
    resume_path = os.path.join("temp_resume_file" + os.path.splitext(resume_file.name)[1])
    jd_path = os.path.join("temp_jd_file" + os.path.splitext(jd_file.name)[1])

    with open(resume_path, "wb") as f:
        f.write(resume_file.getbuffer())
    with open(jd_path, "wb") as f:
        f.write(jd_file.getbuffer())

    resume_text = parser.clean_text(parser.extract_text(resume_path))
    jd_text = parser.clean_text(parser.extract_text(jd_path))

    score = matcher.compute_similarity(resume_text, jd_text)
    st.subheader("Similarity Score")
    st.write(f"**{score:.2f}** (0 = no match, 1 = perfect match)")

    os.remove(resume_path)
    os.remove(jd_path)
else:
    st.info("Please upload both Resume and Job Description to see similarity score.")
