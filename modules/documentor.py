import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_docstring(codesnippet):
    
    prompt = f"""
You are a technical documentation expert
Task: Write a Python docstring for the following function
Constraint: "Return ONLY the docstring text (inside triple quotes). Do not add any conversational text."

{codesnippet}
"""
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"error on calling gemini api{e}")
        return None