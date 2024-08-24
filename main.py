import speech_recognition as sr
import webbrowser
import pyttsx3
import Musiclibray as mp  

engine = pyttsx3.init()
r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def procommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif c.startswith("play"):
        setting = c.split(" ", 1)[1]
        if setting in mp.music:
            sound = mp.music[setting]
            print(f"Playing: {sound}")
            webbrowser.open(sound)
        else:
            speak("Sorry, I couldn't find that song.")
    else:
        speak("Command not recognized.")

print("Listening")

if __name__ == "__main__":
    speak("Hey Jarvis...")
    while True:
        with sr.Microphone() as source:
            audio = r.listen(source, timeout=2, phrase_time_limit=5)
        
        print("Recognizing...")
        try:
            recognized_text = r.recognize_google(audio)
            print(recognized_text)
            if "jarvis" in recognized_text.lower():
                speak("Ya bro")
                with sr.Microphone() as source:
                    print("Activating Jarvis")
                    audio = r.listen(source, phrase_time_limit=3)
                    command = r.recognize_google(audio)
                    print(f"Command: {command}")
                    procommand(command)
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Sorry, there was an issue with the request.")
        except Exception as e:
            print(f"Error: {e}")
