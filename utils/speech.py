import speech_recognition as sr
from gtts import gTTS
import os

def speak(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    os.system("mpg123 response.mp3") # For Linux/Mac. On Windows, use another player.

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("You: ", end="", flush=True)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
        return text
    except Exception as e:
        print("Could not process audio:", e)
        return ""
