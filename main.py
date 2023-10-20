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

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": pregunta["pregunta"]
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return {
        "respuesta": response["choices"][0]["message"]["content"]
    }
