from aiogram import types
from dispatcher import dp
import config
import markup as nav

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Привет!\n Я бот-кодер, помощник программиста\n но пока что я только повторюшка", reply_markup=nav.mainMenu)

@dp.message_handler(text=["Ты писька", "ты писька"])
async def send_message(message: types.Message):

        await message.reply("сам писька")

@dp.message_handler(text=["Ты красавчик", "ты красавчик"])
async def send_message(message: types.Message):

        await message.reply("а ты тоже ничего))")

@dp.message_handler()
async def echo(message: types.Message):

    await message.answer(message.text)


