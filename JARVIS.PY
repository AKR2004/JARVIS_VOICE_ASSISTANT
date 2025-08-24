# ---------------------------------------------
# Project: Jarvis - Personal Voice Assistant
# Author: Aditya kumar (BCA Final Year)
# ---------------------------------------------

# 🔹 Required Libraries
import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import os
import wikipedia
import pyjokes

# 🔹 Initialize recognizer and voice engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Voice customization
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)   # Change [0] / [1] for male/female
engine.setProperty("rate", 160)             # Speed of speech
engine.setProperty("volume", 1.0)           # Max volume

# Speak function
def speak(text):
    """Converts text to speech"""
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# Process user command
def processCommand(command):
    """Execute commands based on user speech"""
    command = command.lower()

    # Website Shortcuts
    if "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "whatsapp" in command:
        speak("Opening WhatsApp Web")
        webbrowser.open("https://web.whatsapp.com")

    elif "facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    # Time & Date
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}")

    elif "date" in command:
        today = datetime.date.today().strftime("%d %B %Y")
        speak(f"Today's date is {today}")

    # Music
    elif "play music" in command or "song" in command:
        music_dir = "C:/Users/Public/Music"   # apna path change karo
        try:
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Playing music")
        except:
            speak("No music found in the folder")

    # Wikipedia
    elif "who is" in command or "what is" in command:
        try:
            result = wikipedia.summary(command, sentences=2)
            speak(result)
        except:
            speak("Sorry, I couldn't find anything on Wikipedia")

    # Jokes
    elif "joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)

    # System Commands
    elif "shutdown" in command:
        speak("Shutting down the system")
        os.system("shutdown /s /t 1")

    elif "restart" in command:
        speak("Restarting the system")
        os.system("shutdown /r /t 1")

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    # News & Weather (via browser)
    elif "news" in command:
        speak("Opening latest news")
        webbrowser.open("https://news.google.com")

    elif "weather" in command:
        speak("Opening weather report")
        webbrowser.open("https://www.weather.com")

    else:
        speak("Sorry, I did not understand that command")

# Main program loop
if __name__ == "__main__":
    speak("Initializing Jarvis...") 
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=3)
            word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes, I'm listening")

                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis active... listening for command")
                    audio = recognizer.listen(source, timeout=4, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    print("Command heard:", command)
                    processCommand(command)

        except Exception as e:
            print("Error:", e)
