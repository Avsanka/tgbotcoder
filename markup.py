from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMainEge = KeyboardButton('ЕГЭ')
btnMainSam = KeyboardButton('Самостоятельное изучение')
btnMainLanHelp = KeyboardButton('Помощь с выбором языка')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMainEge, btnMainSam, btnMainLanHelp)


btnEgePascal = KeyboardButton('Pascal')
btnEgePython = KeyboardButton('Python')
btnEgeCpp = KeyboardButton('C++')
btnBack = KeyboardButton('Back to main')
egeEgeLanMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnEgePascal, btnEgePython, btnEgeCpp, btnBack)

btnSamCs = KeyboardButton('C#')
btnSamCpp = KeyboardButton('C++')
samMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnSamCs,BtnSamCpp,btnBack)

lanHelpMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnBack)

