import speech_recognition as sr
import webbrowser
import os
import sys
import pyttsx3
# Якщо немає звуку

engine = pyttsx3.init()
# engine.say("Say")
# engine.runAndWait()


def talk(words):
    print(words)
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
    # os.system(" say " + words)


talk("Hi, can I help you?")


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say")
        r.pause_threshould = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)


    try:
        task = r.recognize_google(audio, language='ua-UA').lower()
        print('Я вас не зрозумів' + task)
    except sr.UnknownValueError:
        talk("Я вас не зромів")
        task = command()

    return task


def make_something(task):
    if 'open site' in task:
        talk('Відкриваю')
        url = "https://ituniver.com"
        webbrowser.open(url)


while True:
    make_something(command())
