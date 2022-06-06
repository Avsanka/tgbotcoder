from aiogram import types
from aiogram.types import ContentTypes, Message
import markup as nav
import bot
from dispatcher import dp

@dp.message_handler(text='✅Помощь с выбором языка')
async def answer(message: Message):
    await message.reply("Знакомы ли вы с основными терминами?", reply_markup=nav.q1)


@dp.message_handler(text='Да')
async def answer(message: Message):
    await message.reply("Изучали ли вы программирование раньше?", reply_markup=nav.q2)


@dp.message_handler(text='Немного')
async def answer(message: Message):
    await message.reply("Изучали ли вы программирование раньше?", reply_markup=nav.q2)


@dp.message_handler(text='Нет')
async def answer(message: Message):
    await message.reply("Изучали ли вы программирование раньше?", reply_markup=nav.q2)


@dp.message_handler(text='Дa')
async def answer(message: Message):
    await message.reply("Предпочитаете сложный язык программирования или простой?", reply_markup=nav.q3)


@dp.message_handler(text='Пытался')
async def answer(message: Message):
    await message.reply("Предпочитаете сложный язык программирования или простой?", reply_markup=nav.q3)


@dp.message_handler(text='Нeт')
async def answer(message: Message):
    await message.reply("Предпочитаете сложный язык программирования или простой?", reply_markup=nav.q3)


@dp.message_handler(text='Сложный')
async def answer(message: Message):
    await message.reply("С какой целью вы хотите изучать программирование?", reply_markup=nav.q4)


@dp.message_handler(text='Простой')
async def answer(message: Message):
    await message.reply("С какой целью вы хотите изучать программирование?", reply_markup=nav.q4)


@dp.message_handler(text='Что-то между')
async def answer(message: Message):
    await message.reply("С какой целью вы хотите изучать программирование?", reply_markup=nav.q4)


@dp.message_handler(text='Для работы')
async def answer(message: Message):
    await message.reply("Какое у вас образование?", reply_markup=nav.q5)


@dp.message_handler(text='Для учёбы')
async def answer(message: Message):
    await message.reply("Какое у вас образование?", reply_markup=nav.q5)


@dp.message_handler(text='Личный интерес')
async def answer(message: Message):
    await message.reply("Какое у вас образование?", reply_markup=nav.q5)


@dp.message_handler(text='Высшее')
async def answer(message: Message):
    await message.reply("Лучший выбор для вас - C++ || C#", reply_markup=nav.mainMenu)


@dp.message_handler(text='Среднее')
async def answer(message: Message):
    await message.reply("Лучший выбор для вас - Pascal 🔤", reply_markup=nav.mainMenu)


@dp.message_handler(text='Другое')
async def answer(message: Message):
    await message.reply("Лучший выбор для вас - Python 🐍", reply_markup=nav.mainMenu)