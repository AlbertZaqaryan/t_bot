from telebot import TeleBot
from dotenv import load_dotenv
import os

load_dotenv()


TOKEN = os.getenv('TOKEN')
bot = TeleBot(token=TOKEN)

@bot.message_handler(commands=['start'])
def func(message):
    bot.send_message(message.chat.id, "Hello bro 😎😎😎")

@bot.message_handler()
def chat(message):
    if message.text == 'Trainer':
        bot.reply_to(message, "One moment...")
        with open('trainers.txt', 'r', encoding='utf-8') as file:
            bot.send_message(message.chat.id, file.read())

bot.polling()