import streamlit as st
from AIengine import get_ai_response
from VoiceOutput import speak_text
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
gemini_key = os.getenv("GEMINI_API_KEY")


# If using voice input
from VoiceInput import listen_to_user 

def  main():
    print("MentorMate is ready! ")

    if not OpenAI and not gemini_key:
        print("No API keys found! Please check your .env file.")
        return

    while True:
        mode = input("Type 'v' for voice or 't' for text input (or 'quit' to exit): ").lower()

        if mode == 'quit':
                print(" Goodbye!")
                break
        elif mode == 'v':
           try:
                user_input = listen_to_user()
           except Exception as e:
                print(f"Voice input failed: {e}")
                continue     
        elif mode == 't':
                user_input = input("You: ")
        else:
                print("Invalid input mode.")
                continue

        if not user_input.strip():
                continue
 
        ai_response = get_ai_response(user_input)
        print(f"MentorMate: {ai_response}")
        
        try:
            speak_text(ai_response)
        except Exception as e:
            print(f"(Voice Error): {e}")

if __name__ == "__main__":
    main()