import datetime
from flask import request
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import ctypes
from keyboard import press_and_release
import pywhatkit as pwt
import requests
from bs4 import BeautifulSoup

from Speak import speak
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# # print(voices[1].id)
# voices = engine.setProperty('voice', voices[0].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 16:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("hello Atharva i am Jarvis, how can i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")

    except Exception as e:

        print("please say again...")
        return "none"
    return query

def temp(query):
    if 'temperature of' in query:
        url = f"https://www.google.com/search?q={query}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temperature = data.find("div", class_ = "BNeawe").text
        print(f"the temperature is {temperature} celcius")
        speak(f"the temperature is {temperature} celcius")

def chrome_auto(query):
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search' in query:
            search = query.replace("search", "")
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            speak("Here\'s what i found about" + search)

        elif 'open' in query:
            website = query.replace("open ", "")
            url = f'https://www.{website}.com'
            webbrowser.open(url)

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'new tab' in query:
            press_and_release('ctrl + t')

        elif 'close tab' in query:
            press_and_release('ctrl + w')

        elif 'switch to tab' in query:
            no = query.replace("switch to tab", "")
            press_and_release(f"ctrl + {no}")

        elif 'open incognito' in query:
            press_and_release('ctrl + shift + n')

        elif 'facebook' in query:
            name = input("whome do you want to search: ")
            url = f'https://www.facebook.com/search/top/?q={name}'
            webbrowser.open(url)

        elif 'instagram' in query:
            name = input("whome do you want to search: ")
            url = f'https://www.instagram.com/{name}/'
            webbrowser.open(url)

def youtube_auto(query):
        if 'on youtube' in query:
            src = query.replace("on youtube", "")
            url = "https://www.youtube.com/results?search_query=" + src
            webbrowser.open(url)

        elif 'pause' in query:
            press_and_release('k')

        elif 'play' in query:
            press_and_release('k')

        elif 'mute' in query:
            press_and_release('m')

        elif 'unmute' in query:
            press_and_release('m')

        elif 'next video' in query:
            press_and_release('shift + n')

        elif 'previous video' in query:
            press_and_release('shift + p') # ----> previous video is a problem

        elif 'open miniplayer' in query:
            press_and_release('i')

        elif 'caption' in query:
            press_and_release('c')

        elif 'speed up' in query:
            press_and_release('shift + >')

        elif 'slow down' in query:
            press_and_release('shift + <')

        elif 'forward' in query:
            press_and_release('l')

        elif 'backward' in query:
            press_and_release('j')

        elif 'full screen' in query:
            press_and_release('f')

def time(query):
    if 'what\'s the time' in query:
            strTime = datetime.datetime.now().strftime("%H pass %M minutes %S seconds")
            speak(f"the time is {strTime}")

def google_maps(query):
    if 'directions' in query:
        speak("enter source")
        source = input("enter source: ")
        speak("enter destination")
        destination = input("enter destination: ")
        webbrowser.open(f"https://www.google.com/maps/dir/{source}/{destination}")
    elif 'locate' in query:
        loc = query.replace("locate","")
        webbrowser.open(f"https://www.google.com/maps/place/{loc}")

def General_operation(query):
        if 'copy' in query:
            press_and_release('ctrl + c')
            speak('copied')
        
        elif 'Paste' in query:
            press_and_release('ctrl + v')   # ---> paste is a problem

        elif 'cut' in query:
            press_and_release('ctrl + x')

        elif 'underline' in query:
            press_and_release('ctrl + u')

        elif 'bold text' in query:
            press_and_release('ctrl + b')

        elif 'italic text' in query:
            press_and_release('ctrl + i')

        elif 'undo' in query:
            press_and_release('ctrl + z')

        elif 'print' in query:
            press_and_release('ctrl + p')

        elif 'open files' in query:
            press_and_release('ctrl + o')

        elif 'select all' in query:
            press_and_release('ctrl + a')

        elif 'align center' in query:
            press_and_release('ctrl + e')

        elif 'justify' in query: 
            press_and_release('ctrl + j')

        elif 'align left' in query:
            press_and_release('ctrl + l')

        elif 'align right' in query:
            press_and_release('ctrl + r')

        elif 'increase font size' in query:
            press_and_release('ctrl + shift + >') 

        elif 'decrease font size' in query:
            press_and_release('ctrl + shift + <')  

        elif 'subscript' in query:
            press_and_release('ctrl + =')

        elif 'save' in query:
            press_and_release('ctrl + s')

        elif 'new file' in query:
            press_and_release('ctrl + n')

        elif 'close' in query:
            press_and_release('alt + f4')

        elif 'screenshot' in query:
            press_and_release('win + prtscn')

        elif 'lock my device' in query:
            ctypes.windll.user32.LockWorkStation()

        elif 'shut down my device' in query:
            os.system("shutdown /s /t 1")

        elif 'new folder' in query:
            press_and_release('ctrl + shift + n')

def songs(query):
     if 'song' in query:
            song = query.replace("song", "")
            url = 'https://open.spotify.com/search/' + song
            webbrowser.open(url)

def conversation(query):
    if 'hi robo' in query:
        speak('hi how are you')

    elif 'i am fine' in query:
        speak('good to here that')

    elif 'how are you' in query:
        speak('i am fine, thank you')

    elif 'where do you live robo' in query:
        speak('in your device haha')

    elif 'bye' in query:
            speak("bye , nice to meet you")
            exit()

def Whatsapp_auto(query):
    if 'open whatsapp web' in query:
        webbrowser.open("https://web.whatsapp.com/")
    elif 'send a message' in query:
        num = input("enter number: ")
        ms = input("enter the msg: ")
        hr = int(input("hours: "))
        mi = int(input("minutes: "))
        pwt.sendwhatmsg(f"+91{num}", f"{ms}",hr,mi)

def google_meet(query):
    if 'microphone in meet' in query:
        press_and_release('ctrl + d')

    elif 'camera in meet' in query:
        press_and_release('ctrl + e')

    elif 'chat in meet' in query:
        press_and_release('ctrl + alt + c')

    elif 'raise hand in meet' in query:
        press_and_release('ctrl + alt + h')

    elif 'participant in meet' in query:
        press_and_release('ctrl + alt + p')

def My_loc(query):
    if 'my location' in query:   
        ip_adr = requests.get("https://api.ipify.org").text
        url = "https://get.geojs.io/v1/ip/geo/"+ip_adr+".json"
        geo_q = requests.get(url)
        geo_d = geo_q.json()
        state = geo_d['city']
        country = geo_d['country']
        print(f"you are now in {state , country} .")
        speak(f"you are now in {state , country} .")

def alarm(query):
    if 'set alarm' in query:
        speak("enter the time")
        time = input("Enter the time: ")
        while True:
          now = datetime.datetime.now().strftime("%H:%M:%S")
          if now == time:
              speak("time to wake up and do the task")
          elif now>time:
              break

# if __name__ == "__main__":
#     wishme()
#     while True:
#         query = takeCommand().lower()
#         chrome_auto(query)
#         youtube_auto(query)
#         time(query)
#         General_operation(query)
#         songs(query)
#         conversation(query)
#         Whatsapp_auto(query)
#         google_meet(query)
#         temp(query)
#         google_maps(query)
#         My_loc(query)
#         alarm(query)