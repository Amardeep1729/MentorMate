import speech_recognition as sr
def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = recognizer.listen(source)

    try: 
        text = recognizer.recognize_google(audio)
        print(f"You (voice): {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that")
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
    
    return ""