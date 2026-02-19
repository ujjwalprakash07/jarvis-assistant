

#LIBRARIES TO IMPORT
import speech_recognition as sr #speech recognition
import pyttsx3                  #speak lib
import webbrowser               #websearch lib

recognizer = sr.Recognizer()

#for giving random replies
import random
def random_reply(replies):
    return random.choice(replies)

import time
ACTIVE_DURATION = 10   # seconds
active_until = 0

import datetime

def time_greeting():
    hour = datetime.datetime.now().hour

    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 21:
        return "Good evening"
    else:
        return "Good night"



#SPEAK FUNCTION



def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


#Commands
def processCommand(c):
    print("Command:", c)
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")
        return True
    elif "open youtube" in c.lower():
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com/")
        return True
    elif "open chrome" in c.lower():
        speak("Opening chrome")
        webbrowser.open("https://chrome.com")
        return True
    elif "open instagram" in c.lower() or "open insta" in c.lower():
        speak("Opening instagram")
        webbrowser.open("https://instagram.com")
        return True
    elif "open facebook" in c.lower():
        speak("Opening facebook")
        webbrowser.open("https://facebook.com")
        return True
    elif "open github" in c.lower():
        speak("opening github")
        webbrowser.open("https://www.github.com")
        return True
    

        #greet on basis of time
    elif "greet me" in c.lower() or "hello" in c.lower():
        speak(time_greeting())
        return True

        # Casual conversation replies
    elif "kaise ho" in c.lower():
        speak(random_reply([
            "Main bilkul theek hoon, aap kaise ho?",
            "Ek dum mast ",
            "Sab badhiya chal raha hai",
            "Feeling great, aap batao"
        ]))
        return True
    elif "how are you" in c.lower() or "how r u" in c.lower():
        speak(random_reply([
            "i am fine, what about you?",
            "All good, just waiting for your command",
            "Everything is going fine",
            "Feeling great!"
        ]))
        return True
    elif "kya kar raha hai" in c.lower():
        speak(random_reply([
        "Bas tumse baat kar raha hoon",
        "Yahin hoon, sun raha hoon",
        "Kuch khaas nahi, tum batao"
    ]))
        return True

    elif "what are you doing" in c.lower():
        speak(random_reply([
            "Just listening to you",
            "Waiting for your next command",
            "Nothing much, talking to you"
        ]))
        return True
    
    # ===== HELLO / HI =====
    elif "hello" in c or "hi" in c.lower() or "hey" in c.lower():
        speak(random_reply([
            "Hey",
            "Hello",
            "Hi there"
        ]))
        return True


    # ===== THANKS =====
    elif "thank you" in c.lower() or "thanks" in c.lower():
        speak(random_reply([
            "You're welcome",
            "No problem",
            "Anytime"
        ]))
        return True


    # ===== BYE =====
    elif "bye" in c.lower() or "goodbye" in c.lower():
        speak(random_reply([
            "Bye",
            "See you",
            "Talk to you later"
        ]))
        return True


    # ===== BORED =====
    elif "bore ho raha" in c.lower():
        speak(random_reply([
            "Koi baat nahi, baat kar lete hain",
            "Main hoon na",
            "Kuch interesting karein?"
        ]))
        return True

    elif "i am bored" in c.lower() or "bored" in c.lower():
        speak(random_reply([
            "Want to talk about something?",
            "Let's do something fun",
            "I'm here, tell me"
        ]))
        return True
        # ===== NAME =====
    elif "tumhara naam kya hai" in c.lower():
        speak(random_reply([
            "Main Jarvis hoon",
            "Log mujhe Jarvis kehte hain",
            "Main tumhara assistant hoon"
        ]))
        return True

    elif "what is your name" in c.lower() or "who are you" in c.lower():
        speak(random_reply([
            "I'm Jarvis",
            "You can call me Jarvis",
            "I'm your personal assistant"
        ]))
        return True


    # ===== FEELINGS =====
    elif "achha lag raha hai" in c.lower():
        speak(random_reply([
            "Sun ke achha laga",
            "Sahi hai phir",
            "Mood acha hai lagta hai"
        ]))
        return True

    elif "i feel good" in c.lower() or "feeling good" in c.lower():
        speak(random_reply([
            "That's nice",
            "Good to hear that",
            "Glad you're feeling good"
        ]))
        return True


    # ===== TIRED =====
    elif "thak gaya hoon" in c.lower() or "tired hoon" in c.lower():
        speak(random_reply([
            "Thoda rest kar lo",
            "Break lena chahiye",
            "Zyada stress mat lo"
        ]))
        return True

    elif "i am tired" in c.lower():
        speak(random_reply([
            "You should take some rest",
            "Maybe a short break will help",
            "Don't push yourself too hard"
        ]))
        return True


    # ===== HUNGRY =====
    elif "bhook lagi hai" in c.lower():
        speak(random_reply([
            "Kuch kha lo",
            "Khane ka time ho gaya lagta hai",
            "Light sa kuch kha lena"
        ]))
        return True

    elif "i am hungry" in c.lower():
        speak(random_reply([
            "You should eat something",
            "Maybe grab a snack",
            "Food sounds like a good idea"
        ]))
        return True


    # ===== SLEEP =====
    elif "neend aa rahi hai" in c.lower():
        speak(random_reply([
            "So jaana chahiye",
            "Aaram kar lo",
            "Kal fresh feel karoge"
        ]))
        return True

    elif "i am sleepy" in c.lower() or "feeling sleepy" in c.lower():
        speak(random_reply([
            "You should get some sleep",
            "Rest will help",
            "Sleep sounds like a good plan"
        ]))
        return True


    # ===== PRAISE =====
    elif "tum ache ho" in c.lower() or "you are good" in c.lower():
        speak(random_reply([
            "Shukriya",
            "Achha laga sun ke",
            "Tum bhi kaafi ache ho"
        ]))
        return True


    # ===== JOKING =====
    elif "mazaak kar raha hoon" in c.lower():
        speak(random_reply([
            "Samajh gaya",
            "Thik hai, mazaak chalta hai",
            "Funny ho tum"
        ]))
        return True

    elif "just kidding" in c.lower():
        speak(random_reply([
            "Got it",
            "Haha okay",
            "Nice one"
        ]))
        return True


    # ===== THINKING =====
    elif "kya soch raha hai" in c.lower():
        speak(random_reply([
            "Bas yahi soch raha hoon tum kya bologe",
            "Kuch khaas nahi",
            "Random thoughts"
        ]))
        return True

    elif "what are you thinking" in c.lower():
        speak(random_reply([
            "Just random thoughts",
            "Nothing specific",
            "Thinking about what you'll say next"
        ]))
        return True


    # ===== HELP =====
    elif "madad chahiye" in c.lower():
        speak(random_reply([
            "Haan bolo",
            "Kis cheez mein madad chahiye",
            "Batao kya karna hai"
        ]))
        return True

    elif "help me" in c.lower() or "can you help me" in c.lower():
        speak(random_reply([
            "Sure, tell me",
            "What do you need help with?",
            "I'm listening"
        ]))
        return True



# CASUAL TALKS
    elif "tum kaun ho" in c.lower():
        speak("Main aapka personal assistant hoon, Jarvis")
        return True

    elif "who are you" in c.lower():
        speak("I am Jarvis, your personal voice assistant")
        return True

    elif "mera naam kya hai" in c.lower():
        speak("Aapka naam Dhoni hai")
        return True

    elif "thank you" in c.lower() or "thanks" in c.lower():
        speak("You are welcome")
        return True

    elif "bye" in c.lower() or "goodbye" in c.lower():
        speak("Goodbye, take care")
        return True

    elif "good morning" in c.lower():
        speak("Good morning, hope you have a great day")
        return True

    elif "good night" in c.lower():
        speak("Good night, sweet dreams")
        return True

    elif "i love you" in c.lower():
        speak("I appreciate that, but I am here to assist you")
        return True

    elif "bore ho raha hai" in c.lower():
        speak("Koi baat nahi, main hoon na baat karne ke liye")
        return True

    elif "kya tum sun sakte ho" in c.lower():
        speak("Haan sir, main aapki baat sun sakta hoon")
        return True
    else:
        print("Unknown command:", c)
        speak("i didn't undersood that, can you please repeat?")
        return False
        


# INITIALIZING JARVIS
if __name__ == "__main__":
    speak("Initializing jarvis")
    speak("Hi, i  hope you are fine.")

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)


    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio).lower()
            print("Heard:", text)

            current_time = time.time()

            # 🔔 WAKE WORD
            if "jarvis" in text:
                speak("yaa")
                active_until = current_time + ACTIVE_DURATION
                
                continue

            # ⚡ ACTIVE MODE (no wake word needed)
            if current_time <= active_until:
                handeled =  processCommand(text)
                active_until = current_time + ACTIVE_DURATION  # extend time
            else:
                # sleeping mode → stay silent
                pass

        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            speak("Internet problem")



# @Dhoni all rights reserved 2026
# Created by Ujjwal Prakash