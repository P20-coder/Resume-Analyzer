# 🚀 Resume Analyzer & Job Matcher

A full-stack, production-ready AI-powered web application that allows users to upload a resume and compare it with a job description. The application uses OpenAI's GPT models to evaluate job fit, identify skill gaps, and generate actionable improvement suggestions.

## 🧩 Core Features
- **Resume Upload:** Parse PDF resumes using PyPDF.
- **Job Description Input:** Paste target roles and requirements.
- **AI Analysis Engine:** Generates match scores, identifies missing skills, strengths, weaknesses, and optimization tips.
- **Smart Resume Enhancement:** Rewrites resume bullet points to be quantified and ATS-friendly. Download the result!
- **Skill Gap Intelligence:** Identifies top missing skills and provides actionable project ideas.

## 🛠 Tech Stack
- **Backend:** Python, FastAPI
- **Frontend:** Streamlit
- **AI Integration:** OpenAI API
- **Data parsing:** PyPDF

---

## 📦 Setup & Installation

### Prerequisites
- Python 3.9+
- OpenAI API Key

### 1. Clone & Set Up Virtual Environment

```bash
cd resume-analyzer
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Variables
Either place your `OPENAI_API_KEY` in your system environment variables, or create a `.env` file in the root of the project:
```
OPENAI_API_KEY=your_api_key_here
```
(If using `.env`, make sure to add `python-dotenv` handling in `utils/ai_helper.py` by calling `load_dotenv()`)

---

## 🚀 How to Run Locally

Since this tool uses a separate backend (FastAPI) and frontend (Streamlit), you need to run both concurrently.

### Run Backend (FastAPI)
```bash
python app.py
```
This starts the backend on `http://127.0.0.1:8000`.

### Run Frontend (Streamlit)
Open a new terminal window, activate the virtual environment, and run:
```bash
streamlit run frontend/streamlit_app.py
```
This starts the UI dashboard in your web browser.

---

## ☁️ Deployment

### 1. Backend (FastAPI) on Render
- Connect your GitHub repo to Render.
- Create a new "Web Service".
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn app:app --host 0.0.0.0 --port $PORT`
- *Add `OPENAI_API_KEY` to Render environment variables.*

### 2. Frontend (Streamlit) on Streamlit Community Cloud
- Go to `share.streamlit.io`
- Connect your repository.
- Main file path: `frontend/streamlit_app.py`
- *Important:* Update the `API_URL` inside `streamlit_app.py` to point to your new Render Backend URL.

---

*Built with ❤️ utilizing FastAPI & Streamlit.*
