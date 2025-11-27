import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

def audit_code(codesnippet):
    promt = f"""
Role: "You are a Senior Security Engineer and White-Hat Hacker."
Task: "Analyze this code strictly for security vulnerabilities."
Output: "List critical issues found (e.g., hardcoded secrets, injection risks). If safe, say 'No critical vulnerabilities found'."

{codesnippet}
"""
    
    try:
        response = model.generate_content(promt)
        return response.text
    except Exception as e:
        print(f"error on calling gemini api{e}")
        return None