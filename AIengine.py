import os
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai as genai
import threading

# Load API keys
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")
openai_key = os.getenv("OPENAI_API_KEY")

# Init OpenAI client
client = OpenAI(api_key=openai_key)

# Init Gemini
genai.configure(api_key=gemini_key)

# Threaded Gemini call (to support timeout)
def call_gemini(prompt, result_holder):
    try:
        gemini_model = genai.GenerativeModel("models/gemini-1.5-flash")
        full_prompt = (
            '''You are MentorMate, a helpful, professional AI mentor. Your job is to provide clear, concise, and actionable advice in four main areas: 
            1. Education and learning techniques (which also include Astronomy)
            2. Programming and software development 
            3. Career guidance and skill-building 
            4. Productivity and time management

            Always stay on-topic. If a question is unrelated (e.g., jokes, food, entertainment, personal relationships, or inappropriate topics), politely decline and redirect the user back to the supported categories.

            Your tone should be motivating and respectful, suitable for students and professionals. Avoid humor, sarcasm, or casual slang. Always prioritize clarity and usefulness.

            \n\nUser: ''' + prompt
        )
        gemini_response = gemini_model.generate_content(full_prompt)
        result_holder.append(gemini_response.text.strip())
    except Exception as e:
        print(f"[Gemini Error]: {e}")

# Main response function
def get_ai_response(prompt: str) -> str:
    result_holder = []

    # Start Gemini in separate thread with timeout
    gemini_thread = threading.Thread(target=call_gemini, args=(prompt, result_holder))
    gemini_thread.start()
    gemini_thread.join(timeout=5)  # wait max 5 seconds

    # Use Gemini response if available
    if result_holder:
        print("[INFO] Used Gemini model: gemini-1.5-flash")
        return result_holder[0]

    # Fallback to OpenAI
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": '''You are MentorMate, a helpful, professional AI mentor. Your job is to provide clear, concise, and actionable advice in four main areas: 
                1. Education and learning techniques (which also include Astronomy)
                2. Programming and software development 
                3. Career guidance and skill-building 
                4. Productivity and time management

                Always stay on-topic. If a question is unrelated (e.g., jokes, food, entertainment, personal relationships, or inappropriate topics), politely decline and redirect the user back to the supported categories.

                Your tone should be motivating and respectful, suitable for students and professionals. Avoid humor, sarcasm, or casual slang. Always prioritize clarity and usefulness.
                '''},
                {"role": "user", "content": prompt}
            ]
        )
        print(f"[INFO] Used OpenAI model: {response.model}")
        return response.choices[0].message.content.strip()
    except Exception as o_error:
        print(f"[OpenAI Error]: {o_error}")
        return "Sorry, all AI services failed to respond."


# Run locally for test
if __name__ == "__main__":
    reply = get_ai_response("Hello, who are you?")
    print("AI:", reply)
