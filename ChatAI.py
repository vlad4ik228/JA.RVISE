from dotenv import load_dotenv as ld
import os
import openai

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    ld(dotenv_path)

openai.api_key = os.getenv("api_key")

models = openai.Model.list()
# print(models)


def handle_input(user_input):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages = [{"role":"user", "content": user_input}])
    return completion


while True:
     user_input = input("You: ")
     # all_response = handle_input(user_input)
     ai_response = handle_input(user_input).choices[0].message.content
     print(ai_response)