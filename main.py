import speech_recognition as sr
import pyttsx3

# obtain audio from the microphone
engine = pyttsx3.init()
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Audio
engine.say("PyBot thinks you said " + r.recognize_google(audio))
engine.runAndWait()
