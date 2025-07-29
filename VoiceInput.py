import speech_recognition as sr
try:
    import speech_recognition as sr
    mic_enabled = True
except Exception as e:
    print(f"[Mic Error] Voice input will be disabled: {e}")
    mic_enabled = False

def listen_to_user():
    if not mic_enabled:
        return "Voice input not available in this environment."

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except Exception as e:
        return f"[Recognition Error]: {e}"