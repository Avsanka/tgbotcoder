from aiogram import types
from dispatcher import dp
import config

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Привет!\n Я бот-кодер, помощник программиста\n но пока что я только повторюшка")

    @dp.message_handler()
    async def echo(message: types.Message):

        await message.answer(message.text)