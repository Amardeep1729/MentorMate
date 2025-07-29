import os
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai as genai
from logger import log_event

# Load API keys
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")
openai_key = os.getenv("OPENAI_API_KEY")

# Init OpenAI client
client = OpenAI(api_key=openai_key)

# Init Gemini
genai.configure(api_key=gemini_key)

def get_ai_response(prompt: str) -> str:
# Try Gemini first
    try:
        gemini_model = genai.GenerativeModel("models/gemini-1.5-flash")
        gemini_prompt = ( "You are MentorMate, a helpful and focused mentor AI. Only answer questions "
                        "related to learning, education, programming, career guidance, and productivity. "
                        "Politely decline off-topic questions.\n\n"
                        f"User: {prompt}")
        gemini_response = gemini_model.generate_content(gemini_prompt)
        log_event(f"[Gemini] Success - Prompt: {prompt}")
        print("[INFO] Used Gemini model: gemini-1.5-flash")
        return gemini_response.text.strip()
    except Exception as g_error:
        log_event(f"[Gemini] Error - {g_error}")
        print(f"[Gemini Error]: {g_error}")
    
# Then to OpenAI
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[ {"role": "system", "content": "You are MentorMate, a helpful and focused mentor AI. Only answer questions related to learning, education, programming, career guidance, and productivity. Politely decline off-topic questions."},
        {"role": "user", "content": prompt}]
        )
        log_event(f"[OpenAI] Success - Prompt: {prompt}")
        print(f"[INFO] Used OpenAI model: {response.model}")
        return response.choices[0].message.content.strip()
    except Exception as o_error:
        log_event(f"[OpenAI] Error - {o_error}")
        print(f"[OpenAI Error]: {o_error}")
        return "Sorry, all AI services failed to respond."


if __name__ == "__main__":
    reply = get_ai_response("Hello, who are you?")
    print("AI:", reply)

