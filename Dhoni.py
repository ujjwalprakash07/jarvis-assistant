import speech_recognition as sr
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def processCommand(c):
    print("Command:", c)
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com/")
    elif "open chrome" in c.lower():
        speak("Opening chrome")
        webbrowser.open("https://chrome.com")
    elif "open instagram" or "open insta" in c.lower():
        speak("Opening instagram")
        webbrowser.open("https://instagram.com")
    elif "open facebook" in c.lower():
        speak("Opening facebook")
        webbrowser.open("https://facebook.com")
    else:
        speak("I didn't understand")

if __name__ == "__main__":
    speak("hello sir, i  hope you are fine.")

    while True:
        try:
            # STEP 1: Wake word
            with sr.Microphone() as source:
                print("Say jarvis wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source)

            word = recognizer.recognize_google(audio).lower()
            print("Heard:", word)

            if "jarvis"  in word:
                speak("haa")

                # STEP 2: Command
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source)

                    command = recognizer.recognize_google(audio)
                    processCommand(command)
            elif "dhoni" or "ms" or "m s d" or "thala" or "mahi"  in word:
                speak("hii, i am M S Dhoni, Captain,Wicket-keeper batsman")

                # STEP 2: Command
                with sr.Microphone() as source:
                    print("Launching helicopterrr")
                    audio = recognizer.listen(source)

                    command = recognizer.recognize_google(audio)
                    processCommand(command)
            else:
                
                a = input("Enter your query: ")
                if (a.lower() == "open youtube"):
                    speak("Opening Youtube")
                    webbrowser.open("https://www.youtube.com/")
                elif a.lower() == "open google":
                    speak("Opening Google")
                    webbrowser.open("https://google.com")
            
                elif a.lower() == "open chrome":
                    speak("Opening chrome")
                    webbrowser.open("https://chrome.com")
                elif a.lower() == "open instagram" or "open insta":
                    speak("Opening instagram")
                    webbrowser.open("https://instagram.com")
                elif a.lower() == "open facebook":
                    speak("Opening facebook")
                    webbrowser.open("https://facebook.com")
                
                    print("hell nahhhh")
                else:
                    speak("I didn't understand")
                    print("hell nahhhh")
        except sr.UnknownValueError:
            pass
            
