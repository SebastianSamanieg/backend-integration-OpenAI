import os
import openai
import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

"""
- Política de seguridad CORS para permitir el acceso a recursos desde cualquier origen, 
con cualquier método y cualquier cabecera (Segun lo configurado)
"""

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # O reemplaza "*" con la lista de orígenes permitidos.
    allow_methods=["*"],     # O reemplaza "*" con la lista de métodos permitidos (por ejemplo, ["GET", "POST"]).
    allow_headers=["*"],     # O reemplaza "*" con la lista de encabezados permitidos.
    allow_credentials=True,  # Habilita la inclusión de credenciales (cookies, encabezados de autorización, etc.).
    expose_headers=["*"],    # O reemplaza "*" con la lista de encabezados expuestos.
)
@app.get("/")
def root():
    return {
        "Service": "Integracion Back OpenIA"
    }
respuestas_entrenador_pokemon = [
    "¡Es hora de la batalla! ¡Vamos, Pikachu!",
    "Tienes que atraparlos a todos. ¡Vamos, Charizard!",
    "¡Mi Squirtle está listo para la acción!",
    "¡El poder de los Pokémon es asombroso!",
    "¡Prepárate para la lucha, Bulbasaur! Es hora de demostrar nuestro poder.",
    "La victoria es nuestro objetivo, Eevee. ¡A luchar con todo!",
    "Mi Jigglypuff nunca retrocede ante un desafío. ¡Vamos a por ello!",
    "¡Hora de mostrar tu destreza, Gengar! Nadie nos detendrá.",
    "¡Charmander, aviva las llamas de la pasión! La batalla comienza ahora."
]

@app.post("/chat")
def chat(pregunta: dict):
    openai.api_key = os.getenv("API-KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Eres un experto en Pokémon, sabes sobre la historia pokemon, el competitivo pokemon y todo lo que vas a responder gira entorno a pokemon"
            },
            {
                "role": "user",
                "content": pregunta["pregunta"]
            }
        ],
        temperature=1,
        max_tokens=350,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    respuesta_aleatoria = random.choice(respuestas_entrenador_pokemon)
    return {
        "respuesta": response["choices"][0]["message"]["content"] + "\n" + respuesta_aleatoria
    }
