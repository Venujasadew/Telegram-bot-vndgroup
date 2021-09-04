import os
import telebot


bot = telebot.TeleBot("1974339032:AAEQYVYq1L6Xecv-HzNz-awfvSz3VG_yXbA")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm VndGroup Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "")



bot.polling()
