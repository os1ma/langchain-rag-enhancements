import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt="Hello!",
    temperature=0,
)

print(response)
