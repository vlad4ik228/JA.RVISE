import speech_recognition as sr
import webbrowser
import os
import sys
import pyttsx3

# ---------------------------------------------------------
import openai

from dotenv import load_dotenv as ld

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    ld(dotenv_path)

openai.api_key = os.getenv("api_key")

def handle_input(user_input):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": user_input}])
    return completion

# ---------------------------------------------------------y
# Якщо немає звуку
engine = pyttsx3.init()
# engine.say("Say")
# engine.runAndWait()

take = input("Який тип помічника ти хочеш? Обери голосовий (1) чи письмовий (2)")
def talk(words):
    print(words)
    if take == "1":
        engine = pyttsx3.init()
        engine.say(words)
        engine.runAndWait()
        # os.system(" say " + words)


talk("Hi, can I help you?")


def command():
    if take == "1":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say")
            r.pause_threshould = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)


    try:
        task = r.recognize_google(audio, language='uk-UA').lower()
        print('відкриваю' + task)
    except sr.UnknownValueError:
        talk("Я вас не зромів")
        task = command()
    else:
        task = input("Your task: ")

    return task


def make_something(task):
    if 'відкрий' and "сайт" in task:
        talk('Відкриваю')
        url = "https://ituniver.com"
        webbrowser.open(url)


    elif "ім'я" and "твое" in task:
        talk("I am Groot")


    elif "стоп" in task:
        talk("До побачення")
        sys.exit()


    else:
        try:
            ai_response = handle_input(task).choices[0].message.content
            talk(ai_response)
        except openai.error.ServiceUnavailableError:
            talk("Sorry, I am going to try again")
            try:
                ai_response = handle_input(task).choices[0].message.content
                talk(ai_response)
            except openai.error.ServiceUnavailableError:
                talk("Sorry, can you give me the new task?")


while True:
    make_something(command())
