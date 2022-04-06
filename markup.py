from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnBack = KeyboardButton('⏮Back to main')

btnMainEge = KeyboardButton('📚ЕГЭ')
btnMainSam = KeyboardButton('🤓 Самостоятельное изучение')
btnMainLanHelp = KeyboardButton('✅Помощь с выбором языка')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(btnMainEge, btnMainSam, btnMainLanHelp)


btnEgePascal = KeyboardButton('🔤Pascal')
btnEgePython = KeyboardButton('🐍Python')
btnEgeCpp = KeyboardButton('➕C++')
egeLanMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnEgePascal, btnEgePython, btnEgeCpp, btnBack)

btnSamCs = KeyboardButton('C#')
btnSamCpp = KeyboardButton('C++')
samMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(btnSamCs, btnSamCpp, btnBack)

lanHelpMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(btnBack)

