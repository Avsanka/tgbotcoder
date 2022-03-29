from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnOne = KeyboardButton('Test button')
btnTwo = KeyboardButton('Test button 2')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnOne, btnTwo)
