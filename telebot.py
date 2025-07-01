import Telebot

# Reemplaza con tu token de bot
BOT_TOKEN = '6973429821:AAGmCkWXIvHMN7yy_WbXcMNDoYP_zVHGaNk'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
