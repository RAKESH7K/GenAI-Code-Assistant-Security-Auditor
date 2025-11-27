import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

def start_chat(codesnippet):
    print("chat mode started (type 'exit' to quit)")
    print("_______________________________________")


    chat_session = model.start_chat(history=[
        {"role": "user", "parts": [f"Here is the code context:\n{codesnippet}"]}
    ])

    while True:
        user_question = input("\you")
        if user_question.lower() in ["exit" ,"quit"]:
            print("quitting chat bie")
            break

        try:
            response =chat_session.send_message(user_question)
            print(f"gemini:{response.text}")
        except Exception as e:
            print(f"ERROR:{e}")
        
