#!/opentty.py rundll
#
#  This code is part of OpenTTY Service Library
#  ChatGPT [Config.] Advanced client


global openai

import openai

openai.api_key = library['openai-apikey']


def chat_with_gpt3(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

while True:
    user_input = input(f"&username: ")
    if user_input.lower() == "/exit": break
    if user_input.lower() == "/clear": app.clear()

    prompt = f"You: {user_input}\nChatGPT:"
    response = chat_with_gpt3(prompt)
    print("ChatGPT:", response)