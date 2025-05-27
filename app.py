from flask import Flask, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Carga la clave API de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Base de datos simulada de propiedades
propiedades = [
    {"ubicacion": "Miraflores", "tipo": "departamento", "precio": "180000", "habitaciones": 3},
    {"ubicacion": "Cusco", "tipo": "casa", "precio": "120000", "habitaciones": 4},
    {"ubicacion": "Piura", "tipo": "departamento", "precio": "95000", "habitaciones": 2},
]

def buscar_propiedades(mensaje):
    resultados = [p for p in propiedades if p["ubicacion"].lower() in mensaje.lower()]
    if resultados:
        return "\n".join([f'{p["tipo"].title()} en {p["ubicacion"]} por S/ {p["precio"]}' for p in resultados])
    return "No encontré propiedades que coincidan con tu búsqueda."

@app.route("/webhook", methods=["POST"])
def webhook():
    mensaje_usuario = request.form.get("Body", "")
    respuesta_bot = buscar_propiedades(mensaje_usuario)
    return f"""
        <Response>
            <Message>{respuesta_bot}</Message>
        </Response>
    """

if __name__ == "__main__":
    app.run(debug=True)