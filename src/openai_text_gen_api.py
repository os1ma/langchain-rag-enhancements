import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

# Completions API
response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt="Hello!",
    temperature=0,
)
print(response)

# Chat Completions API
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Hello! I'm Oshima.",
        },
        {
            "role": "assistant",
            "content": "Nice to meet you, Oshima! How can I assist you today?",
        },
        {
            "role": "user",
            "content": "Please introduce yourself.",
        },
    ],
    temperature=0,
)
print(response)
