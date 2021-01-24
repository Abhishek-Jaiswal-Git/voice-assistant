# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 20:21:36 2020

@author: abhis
"""

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser as wb
import win32com.client
import pyjokes
speaker=win32com.client.Dispatch('SAPI.SpVoice')

speaker.speak("hey sir,I am jarvis, how may i help you")
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
wb=wb.get(chrome_path)

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.pause_threshold=0.7
            listener.energy_threshold=1000
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'facebook' in command:
        speaker.speak('opening ')
        wb.open('https://www.facebook.com/')
    elif 'instagram' in command:
        speaker.speak('opening ')
        wb.open('https://www.instagram.com/')
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
