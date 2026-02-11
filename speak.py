# import pyttsx3

# engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# speak("Hello Dhoni, I am speaking")
# a = input("hhh: ")
# if a.lower() == "hyy":
#     speak("hello")
import speech_recognition as sr

import pyttsx3
recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

speak("Hello Dhoni, I am speaking")


if __name__ == "__main__":
    speak("hello, sir")

    while True:
        try:
            # STEP 1: Wake word
            with sr.Microphone() as source:
                print("Listening ")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source)
            word = recognizer.recognize_google(audio).lower()
            print("Heard:", word)
                
            # if a.lower() == "hyy":
            #     speak("hello,i am fine.What about you?")
            if word.lower()== "jarvis":
                speak("hello,i am fine.What about you?")
            else:
                print("sorry")
        except :
            pass
a = input("hhh: ")
if a.lower() == "hyy":
    speak("hello,i am fine.What about you?")

