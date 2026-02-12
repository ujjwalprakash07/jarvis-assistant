
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
    elif "open youtube" in c.lower():
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com/")
    elif "open chrome" in c.lower():
        speak("Opening chrome")
        webbrowser.open("https://chrome.com")
    elif "open instagram" in c.lower() or "open insta" in c.lower():
        speak("Opening instagram")
        webbrowser.open("https://instagram.com")
    elif "open facebook" in c.lower():
        speak("Opening facebook")
        webbrowser.open("https://facebook.com")
    elif "open github" in c.lower():
        speak("opening github")
        webbrowser.open("https://www.github.com/")
    

        # Casual conversation replies
    elif "kaise ho" in c.lower():
        speak(random_reply([
            "Main bilkul theek hoon, aap kaise ho?",
            "Ek dum mast ",
            "Sab badhiya chal raha hai",
            "Feeling great, aap batao"
        ]))
    elif "how are you" in c.lower() or "how r u" in c.lower():
        speak(random_reply([
            "i am fine, what about you?",
            "All good, just waiting for your command",
            "Everything is going fine",
            "Feeling great!"
        ]))
    elif "kya kar raha hai" in c.lower():
        speak(random_reply([
        "Bas tumse baat kar raha hoon",
        "Yahin hoon, sun raha hoon",
        "Kuch khaas nahi, tum batao"
    ]))

    elif "what are you doing" in c.lower():
        speak(random_reply([
            "Just listening to you",
            "Waiting for your next command",
            "Nothing much, talking to you"
        ]))
    
    # ===== HELLO / HI =====
    elif "hello" in c or "hi" in c.lower() or "hey" in c.lower():
        speak(random_reply([
            "Hey",
            "Hello",
            "Hi there"
        ]))


    # ===== THANKS =====
    elif "thank you" in c.lower() or "thanks" in c.lower():
        speak(random_reply([
            "You're welcome",
            "No problem",
            "Anytime"
        ]))


    # ===== BYE =====
    elif "bye" in c.lower() or "goodbye" in c.lower():
        speak(random_reply([
            "Bye",
            "See you",
            "Talk to you later"
        ]))


    # ===== BORED =====
    elif "bore ho raha" in c.lower():
        speak(random_reply([
            "Koi baat nahi, baat kar lete hain",
            "Main hoon na",
            "Kuch interesting karein?"
        ]))

    elif "i am bored" in c.lower() or "bored" in c.lower():
        speak(random_reply([
            "Want to talk about something?",
            "Let's do something fun",
            "I'm here, tell me"
        ]))
        # ===== NAME =====
    elif "tumhara naam kya hai" in c.lower():
        speak(random_reply([
            "Main Jarvis hoon",
            "Log mujhe Jarvis kehte hain",
            "Main tumhara assistant hoon"
        ]))

    elif "what is your name" in c.lower() or "who are you" in c.lower():
        speak(random_reply([
            "I'm Jarvis",
            "You can call me Jarvis",
            "I'm your personal assistant"
        ]))


    # ===== FEELINGS =====
    elif "achha lag raha hai" in c.lower():
        speak(random_reply([
            "Sun ke achha laga",
            "Sahi hai phir",
            "Mood acha hai lagta hai"
        ]))

    elif "i feel good" in c.lower() or "feeling good" in c.lower():
        speak(random_reply([
            "That's nice",
            "Good to hear that",
            "Glad you're feeling good"
        ]))


    # ===== TIRED =====
    elif "thak gaya hoon" in c.lower() or "tired hoon" in c.lower():
        speak(random_reply([
            "Thoda rest kar lo",
            "Break lena chahiye",
            "Zyada stress mat lo"
        ]))

    elif "i am tired" in c.lower():
        speak(random_reply([
            "You should take some rest",
            "Maybe a short break will help",
            "Don't push yourself too hard"
        ]))


    # ===== HUNGRY =====
    elif "bhook lagi hai" in c.lower():
        speak(random_reply([
            "Kuch kha lo",
            "Khane ka time ho gaya lagta hai",
            "Light sa kuch kha lena"
        ]))

    elif "i am hungry" in c.lower():
        speak(random_reply([
            "You should eat something",
            "Maybe grab a snack",
            "Food sounds like a good idea"
        ]))


    # ===== SLEEP =====
    elif "neend aa rahi hai" in c.lower():
        speak(random_reply([
            "So jaana chahiye",
            "Aaram kar lo",
            "Kal fresh feel karoge"
        ]))

    elif "i am sleepy" in c.lower() or "feeling sleepy" in c.lower():
        speak(random_reply([
            "You should get some sleep",
            "Rest will help",
            "Sleep sounds like a good plan"
        ]))


    # ===== PRAISE =====
    elif "tum ache ho" in c.lower() or "you are good" in c.lower():
        speak(random_reply([
            "Shukriya",
            "Achha laga sun ke",
            "Tum bhi kaafi ache ho"
        ]))


    # ===== JOKING =====
    elif "mazaak kar raha hoon" in c.lower():
        speak(random_reply([
            "Samajh gaya",
            "Thik hai, mazaak chalta hai",
            "Funny ho tum"
        ]))

    elif "just kidding" in c.lower():
        speak(random_reply([
            "Got it",
            "Haha okay",
            "Nice one"
        ]))


    # ===== THINKING =====
    elif "kya soch raha hai" in c.lower():
        speak(random_reply([
            "Bas yahi soch raha hoon tum kya bologe",
            "Kuch khaas nahi",
            "Random thoughts"
        ]))

    elif "what are you thinking" in c.lower():
        speak(random_reply([
            "Just random thoughts",
            "Nothing specific",
            "Thinking about what you'll say next"
        ]))


    # ===== HELP =====
    elif "madad chahiye" in c.lower():
        speak(random_reply([
            "Haan bolo",
            "Kis cheez mein madad chahiye",
            "Batao kya karna hai"
        ]))

    elif "help me" in c.lower() or "can you help me" in c.lower():
        speak(random_reply([
            "Sure, tell me",
            "What do you need help with?",
            "I'm listening"
        ]))



# CASUAL TALKS
    elif "tum kaun ho" in c.lower():
        speak("Main aapka personal assistant hoon, Jarvis")

    elif "who are you" in c.lower():
        speak("I am Jarvis, your personal voice assistant")

    elif "mera naam kya hai" in c.lower():
        speak("Aapka naam Dhoni hai")

    elif "thank you" in c.lower() or "thanks" in c.lower():
        speak("You are welcome")

    elif "bye" in c.lower() or "goodbye" in c.lower():
        speak("Goodbye, take care")

    elif "good morning" in c.lower():
        speak("Good morning, hope you have a great day")

    elif "good night" in c.lower():
        speak("Good night, sweet dreams")

    elif "i love you" in c.lower():
        speak("I appreciate that, but I am here to assist you")

    elif "bore ho raha hai" in c.lower():
        speak("Koi baat nahi, main hoon na baat karne ke liye")

    elif "kya tum sun sakte ho" in c.lower():
        speak("Haan sir, main aapki baat sun sakta hoon")
    else:
        pass


# INITIALIZING JARVIS
if __name__ == "__main__":
    speak("Initializing jarvis")
    speak("Hi, i  hope you are fine.")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
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
                processCommand(text)
                active_until = current_time + ACTIVE_DURATION  # extend time
            else:
                # sleeping mode → stay silent
                pass

        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            speak("Internet problem")

