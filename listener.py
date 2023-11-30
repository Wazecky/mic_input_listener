import speech_recognition as sr
import pyaudio

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error: {e}")