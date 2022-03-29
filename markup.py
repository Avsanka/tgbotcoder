from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMainEge = KeyboardButton('Егэ')
btnMainSam = KeyboardButton('Самостоятельное изучение')
btnMainLanHelp = KeyboardButton('Помощь с выбором языка')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMainEge, btnMainSam, btnMainLanHelp)


btnPascal = KeyboardButton('Pascal')
btnPython = KeyboardButton('Python')
btnCpp = KeyboardButton('C++')
btnBack = KeyboardButton('Back to main')
egeLanMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPascal, btnPython, btnCpp, btnBack)

btnCs = KeyboardButton('C#')
samMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCs, btnBack)

lanHelpMenu = ReplyKeyboardMarkup(btnBack)

