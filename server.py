import telebot
import time
from flask import Flask, request

TELEGRAM_TOKEN = "7926885285:AAGTZZ04Im-3lPTFEp_vh-w8mRDSTZKfNsA"

# Instanciamos la API de Telegram
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Flask setup
WEBHOOK_HOST = 'solountelebotbasico.onrender.com'  # Tu dominio de Render
WEBHOOK_PORT = 443  # Puerto HTTPS
WEBHOOK_LISTEN = '0.0.0.0'  # Escucha en todas las interfaces
WEBHOOK_URL_BASE = f"https://{WEBHOOK_HOST}:{WEBHOOK_PORT}"
WEBHOOK_URL_PATH = "/{TELEGRAM_TOKEN}"  # Debe ser único

web_server = Flask(__name__)

# Route to handle webhook requests
@web_server.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
        bot.process_new_updates([update])
        return "OK", 200
    else:
        return "Invalid request", 400

# Handle /start command
@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, "HOLA", parse_mode="html")

# Handle text messages
@bot.message_handler(content_types=['text'])
def bot_texto(message):
    bot.send_message(message.chat.id, message.text, parse_mode="html")

if __name__ == '__main__':
    print("Iniciando el bot")

    # Remove webhook, it fails sometimes the set if there is a previous webhook
    try:
        bot.delete_webhook()
    except Exception as e:
        print(f"Failed to delete previous webhook: {e}")

    time.sleep(2)

    # Set webhook
    try:
        bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH)
        print(f"Webhook set to {WEBHOOK_URL_BASE + WEBHOOK_URL_PATH}")
    except Exception as e:
        print(f"Failed to set webhook: {e}")

    # Start the Flask server
    web_server.run(host=WEBHOOK_LISTEN, port=WEBHOOK_PORT)