import os
import openai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

"""
- Política de seguridad CORS para permitir el acceso a recursos desde cualquier origen, 
con cualquier método y cualquier cabecera (Segun lo configurado)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # O reemplaza "*" con la lista de orígenes permitidos.
    allow_methods=["*"],        # O reemplaza "*" con la lista de métodos permitidos (por ejemplo, ["GET", "POST"]).
    allow_headers=["*"],        # O reemplaza "*" con la lista de encabezados permitidos.
    allow_credentials=True,     # Habilita la inclusión de credenciales (cookies, encabezados de autorización, etc.).
    expose_headers=["*"],       # O reemplaza "*" con la lista de encabezados expuestos.
)
"""

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
