# Chatbot Inmobiliario con Flask + OpenAI

## Requisitos
- Python 3.8+
- Cuenta en OpenAI
- Cuenta Twilio WhatsApp Sandbox (gratuita)
- Ngrok (para exponer localhost)

## Instalación

```bash
git clone https://github.com/tuusuario/chatbot-inmuebles.git
cd chatbot-inmuebles
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requirements.txt
```

## Ejecutar el bot

```bash
python app.py
```

## Exponer con ngrok

```bash
ngrok http 5000
```

Pega la URL en el webhook de Twilio Sandbox.

## Probar en WhatsApp

Escribe:
- "Busco un departamento en Miraflores"
- "¿Tienes casas en Cusco?"