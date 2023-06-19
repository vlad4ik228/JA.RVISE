import speech_recognition as sr
import os
import sys
import pyttsx3
# Якщо немає звуку

engine = pyttsx3.init()
engine.say("Say")
engine.runAndWait()


def talk(words):
    print(words)
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
    #os.system(" say " + words)


talk("Hi, can I help you?")

