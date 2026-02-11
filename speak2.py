import speech_recognition as sr
import pyttsx3
import time

recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()   # re-init = stable
    engine.say(text)
    engine.runAndWait()
    engine.stop()

print("Say 'Jarvis'...")

while True:
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)

        word = recognizer.recognize_google(audio).lower()
        print("Heard:", word)

        if "jarvis" in word:
            speak("Yes sir, how may I help you")
            time.sleep(0.7)   # important pause

    except sr.UnknownValueError:
        pass
    except Exception as e:
        print("Error:", e)
