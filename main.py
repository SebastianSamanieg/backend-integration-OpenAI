import os
import openai
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "Service": "Integracion Back OpenIA"
    }


@app.post("/chat")
def chat(pregunta: dict):
    openai.api_key = "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"

    print(pregunta)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": "Quien es Messi?"
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response)
    return {
        "Service": "Esta intentando chatear"
    }
