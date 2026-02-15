🤖 Jarvis – Personal Voice Assistant (Python)

Jarvis is a Python-based personal voice assistant that listens to voice commands and performs tasks like opening websites, responding to casual conversations, and interacting naturally with the user.

This project is designed to run locally on a PC and is built step-by-step to understand how voice assistants work.

✨ Features

🎤 Voice-controlled assistant

🔑 Wake word support ("jarvis")

🌐 Open popular websites (Google, YouTube, Instagram, etc.)

💬 Casual conversation (English + Hindi)

🎲 Randomized friendly replies

🗣️ Text-to-Speech responses

🖥️ Runs completely on local machine

🧠 Clean and extensible code structure

🛠️ Technologies Used

Python 3

speech_recognition – for speech-to-text

pyttsx3 – for text-to-speech (offline)

webbrowser – to open websites

random – for dynamic replies

time – for active-mode handling

📂 Project Structure
Jarvis/
│
├── Jarvis.py        # Main Jarvis code
├── README.md        # Project documentation
└── requirements.txt (optional)

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/jarvis.git
cd jarvis

2️⃣ Install required libraries
pip install speechrecognition pyttsx3 pyaudio


⚠️ Note:
If pyaudio fails on Windows, install it using a precompiled wheel.

▶️ How to Run
python Jarvis.py


Jarvis will start listening for the wake word.

🎤 How to Use

Say “jarvis”

Jarvis replies with “yaa”

Give a command like:

open google

open youtube

kaise ho

what are you doing

Jarvis responds or performs the action

🗣️ Example Commands
Web Commands

open google

open youtube

open instagram

open facebook

open github

Casual Talk

kaise ho

what are you doing

i am bored

how are you

thank you

bye

🚧 Current Limitations

Requires internet for Google speech recognition

Wake word must be spoken clearly

Local app opening (calculator, VS Code) not yet implemented

Sleep/timeout mode is currently disabled

🚀 Future Improvements

🔒 Offline speech recognition (Vosk / Whisper)

📴 Proper sleep & idle mode

📂 Open local apps and folders

🎵 Music playback

🧩 Modular command system

🖼️ GUI interface

👨‍💻 Author

Ujjwal Prakash
Aspiring Software Developer & AI Enthusiast

⭐ Support

If you like this project:

⭐ Star the repository

🍴 Fork it

🧠 Suggest improvements
