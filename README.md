# VisionATS

# AI Resume & Job Description Matcher

VisionATS is a simple **AI-powered ATS (Applicant Tracking System) tool** that matches resumes against job descriptions and computes similarity scores.  
It helps candidates understand how well their resume fits a job posting, and gives recruiters a quick view of candidate-job fit.

---

#  Features
- Upload resumes (PDF/DOCX) and job descriptions.
- Extracts and cleans text automatically.
- Converts text to embeddings using NLP.
- Computes similarity scores between resumes and JDs.
- Streamlit-based UI for easy interaction.
- Modular project structure with `src/`, `data/`, and `notebooks/`.

---

# Project Structure
VisionATS/
│── Data/ # Sample resumes and job descriptions

│── Notebooks/ # Experimentation notebooks

│── src/ # Core code: parser, matcher, utils

│── app/ # Streamlit frontend

│── requirements.txt # Dependencies

│── README.md # Project documentation




# Installation

## 1. Clone the repo
```bash
git clone https://github.com/Nidhinkdvr/VisionATS.git
cd VisionATS


2. Create a virtual environment and install requirements

python -m venv myenv

myenv\Scripts\activate

pip install -r requirements.txt


3. Run Streamlit app

cd app

streamlit run streamlit_app.py


Example Output:

resume-sample.pdf vs sample-job-description.pdf similarity: 0.36

