
import google.generativeai as genai
import os
from dotenv import load_dotenv
print("reviewer.py loaded successfully")
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)


model = genai.GenerativeModel("gemini-2.5-flash")


def review_code(code_content):
    full_promt = f"""
You are an expert Code Reviewer. Detect the programming language and analyze the following code and provide a detailed review.

Structure your response with these headings:
1. Code Quality
2. Bug Detection
3. Improvement Suggestions
4. Best Practices
--- CODE TO REVIEW ---
{code_content}
"""
    
    try:
        response = model.generate_content(full_promt)
        return response.text
    except Exception as e:
        print(f"Error calling Gemini API:{e}")
        return None
    