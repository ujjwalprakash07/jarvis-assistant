# raw  codeeee...
# only for practice

import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def processCommand(c): 
    if "open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://google.com") 
    elif "open youtube" in c.lower() or "open yt" in c.lower(): 
        webbrowser.open("https://youtube.com") 
    elif "open leetcode" in c.lower(): 
        webbrowser.open("https://leetcode.com/")
    
    

if __name__ == "__main__":
    speak("hello, sir")

    #listen for wake word
    while True:
        r = sr.Recognizer()
        print("recognizing...")
       
            

        

        try:
            # with sr.Microphone() as source:
            #     print("listening")
            #     audio = r.listen(source)
            # word = r.recognize_google(audio)
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source)

            # word = recognizer.recognize_google(audio).lower()
            # print("Heard:", word)
            # if(word.lower() == "good" or word.lower() == "jarvis"):
            #     speak("haa")
            #     with sr.Microphone() as source:
            #         print("Dhoni on strike...")
            #         audio = r.listen(source)
            #         c = r.recognize_google(audio)
            word = recognizer.recognize_google(audio).lower()
            print("Heard:", word)

            if "jarvis" in word:
                speak("haa")
            if(word.lower()=="jarvis" or word.lower()=="dhoni"):
                speak("Yes..")
                with sr.Microphone() as source:
                    print("Jarvis Active ... ")
                    audio = r.listen(source,timeout=2,phrase_time_limit=1)
                    command=r.recognize_google(audio)
                    processCommand(command)

               
                
           
        
        except Exception as e:
            print("Error; {0}".format(e))

