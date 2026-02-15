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
                time.sleep(0.3)
                speak("yaa")
                active_until = current_time + ACTIVE_DURATION
                continue

            # ⚡ ACTIVE MODE (no wake word needed)
            if current_time <= active_until:
                mood = detect_mood(text.lower())
                processCommand(text,mood)
                active_until = current_time + ACTIVE_DURATION  # extend time
            else:
                # sleeping mode → stay silent
                pass

        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            speak("Internet problem")

