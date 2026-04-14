import google.generativeai as genai
import os
from dotenv import load_dotenv

# 👇 explicitly load .env.local
load_dotenv(dotenv_path=".env.local")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env.local")

genai.configure(api_key=api_key)

# Debug: list available models
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)