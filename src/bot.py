import telebot
from dotenv import load_dotenv
import os

load_dotenv()
bot = telebot.TeleBot(str(os.getenv('TELEGRAM_TOKEN')), parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "please send the link of the item you want to be tracked:")



@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()