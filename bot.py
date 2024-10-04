import config
import asyncio

from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot('token')


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hi, I am EchoBot.\nJust write me something and I will repeat it!'
    await bot.reply_to(message, text)





@bot.message_handler(commands=['info'])
async def info_message(message):
    info = 'Я родился вчера но уже могу рассказать o cebe меня зовут Спивагон и я родился для Джоджо референса всё'
    bot.reply_to(message, info)

asyncio.run(bot.polling())