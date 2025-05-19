import pyttsx3
import speech_recognition as sr
import eel
import time

@eel.expose
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    print(voices)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = r.listen(source, timeout=15, phrase_time_limit=10)
            print('Recognizing...')
            eel.DisplayMessage('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            eel.DisplayMessage(query)
            speak(query)
            eel.ShowHood()
        
        except Exception as e:
            print(f"Error: {e}")
            eel.DisplayMessage("Sorry, I couldn't hear you.")
            return ""
