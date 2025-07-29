# import os

# try:
#     import pyttsx3
#     engine = pyttsx3.init()
#     voice_enabled = True
# except Exception as e:
#     print(f"[Voice Error] Voice output will be disabled: {e}")
#     voice_enabled = False

# def speak_text(text):
#     if voice_enabled:
#         engine.say(text)
#         engine.runAndWait()

# def stop_speaking():
#     if voice_enabled:
#         engine.stop()

import streamlit as st

def speak_with_browser(text):
    st.components.v1.html(f"""
        <script>
            var msg = new SpeechSynthesisUtterance({text!r});
            window.speechSynthesis.speak(msg);
        </script>
    """, height=0)

def stop_speaking():
    st.components.v1.html("""
        <script>
            window.speechSynthesis.cancel();
        </script>
    """, height=0)