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
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"},
    ],
    temperature=0,
)
print(response)
