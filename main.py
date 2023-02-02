from dataclasses import replace
from doctest import master
from email.mime import audio
import queue
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition 
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

# print("Initializing jarvis")1

MASTER = "Dev"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak fuction will pronouce the string with passed to it
def speak (text):
    engine.say(text)
    engine.runAndWait()

# This fuction will wish you as per the current time
def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour>= 0 and hour <12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour <18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening"+ MASTER)

    #speak("I am jarvis. How may I help you..?")

# This function will take command from the microphone
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print("Say that again please")
        query = None
    return query

# ************* sending mail funcion *****************
def sendEmail(to, content):
    server =smtplib.SMTP('smtp.gmail.com, 587')
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')
    server.sendmail("devendrabaghel272@gmail.com", to, content)
    server.close()
def main():
    # Main program start here...
    # speak("Initializing jarvis...")   
    wishme()
    query=takecommand()

    # Logic for exexuting tasks as per knowledge

    if 'wikipedia' in query.lower():
        speak('searching wikkipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        # webbrowser.open("youtube.com")
        url = "youtube.com"
        # Windows
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    # Play Songs
    elif 'play music' in query.lower():
        songs_dir = "C:\\Users\\dell\\Downloads\\Ummy Downloads"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{master} the time is {strTime}")

    elif 'open code' in query.lower():
            codePath = "C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code.exe"
            os.startfile(codePath)

    # ***************  Send Emails  ************************
    elif 'email to dev' in query.lower()
        try:
            speak("what should I send")
            content = takecommand()
            to = "devendrabaghel272@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent successfully")

        except Exception as e:
                print(e)