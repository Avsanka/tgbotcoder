from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnOne = KeyboardButton('left')
btnTwo = KeyboardButton('right')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnOne, btnTwo)


btnSuper = KeyboardButton('changed')
btnClassic = KeyboardButton('heeeeyoooh')
btnBack = KeyboardButton('Back to main')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnClassic, btnSuper, btnBack)
