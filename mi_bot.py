import telebot

BOT_TOKEN = '6973429821:AAGmCkWXIvHMN7yy_WbXcMNDoYP_zVHGaNk'  # Reemplaza con tu token real

bot = telebot.Bot(token=BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hola! Bienvenido a mi bot. Usa /chiste para obtener un chiste.")

@bot.message_handler(commands=['chiste'])
def send_joke(message):
    chistes = [
        "¿Por qué los programadores prefieren el color negro? Porque tienen más #.",
        "Un hombre entra a un bar con un cubo de cemento...El camarero le dice: ¿Pide algo?, El hombre responde: Nop. Solo estoy esperando que se seque el cemento.",
        "¿Qué le dice un pez a otro pez?",
        "Nada"
    ]
    import random
    bot.reply_to(message, random.choice(chistes))

bot.infinity_polling()
