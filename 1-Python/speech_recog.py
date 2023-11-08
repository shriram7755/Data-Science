import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
        return ""

def process_command(command):
    if "hello" in command:
        return "Hello, how can I help you?"
    elif "how are you" in command:
        return "I'm fine, thank you!"
    elif "what's your name" in command:
        return "I am your voice assistant."
    elif "exit" in command:
        return "Goodbye!"
    else:
        return "Sorry, I cannot help with that."

def main():
    speak("Rahul tuzya aichi gaand Rahul tuzya aichi gaand  Rahul tuzya aichi gaand  Rahul tuzya aichi gaand  Rahul tuzya aichi gaand ")
     
    while True:
        command = listen()
        if "exit" in command:
            speak("Goodbye!")
            break
        response = process_command(command)
        speak(response)

if _name_ == "_main_":
    main()