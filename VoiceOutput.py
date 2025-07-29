import os

try:
    import pyttsx3
    engine = pyttsx3.init()
    voice_enabled = True
except Exception as e:
    print(f"[Voice Error] Voice output will be disabled: {e}")
    voice_enabled = False

def speak_text(text):
    if voice_enabled:
        engine.say(text)
        engine.runAndWait()

def stop_speaking():
    if voice_enabled:
        engine.stop()