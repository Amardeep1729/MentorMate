import pyttsx3

engine = pyttsx3.init()
is_speaking = False 

def speak_text(text: str):
    engine = pyttsx3.init()
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.say(text)
    engine.runAndWait()

def stop_speaking():
    global is_speaking
    if is_speaking:
        engine.stop()
        is_speaking = False