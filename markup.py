from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnBack = KeyboardButton('⏮В главное меню')

btnMainEge = KeyboardButton('📚ЕГЭ')
btnMainSam = KeyboardButton('🤓 Самостоятельное изучение')
btnMainLanHelp = KeyboardButton('✅Помощь с выбором языка')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(btnMainEge, btnMainSam, btnMainLanHelp)


btnEgePascal = KeyboardButton('🔤Pascal')
btnEgePython = KeyboardButton('🐍Python')
btnEgeCpp = KeyboardButton('➕C++')
egeLanMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnEgePascal, btnEgePython, btnEgeCpp, btnBack)

btnSamCs = KeyboardButton('#️⃣C#')
btnSamPython = KeyboardButton('🐍Pythоn')
btnSamPascal = KeyboardButton('🔤Pascаl')
samMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnSamCs, btnSamPython, btnSamPascal, btnBack)

btnSamCs1 = KeyboardButton('Первая C#')
btnSamCs2 = KeyboardButton('Вторая C#')
btnSamCs3 = KeyboardButton('Третья C#')
SamCsMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnSamCs1, btnSamCs2, btnSamCs3, btnBack)

btnSamPython1 = KeyboardButton('Первая 🐍')
btnSamPython2 = KeyboardButton('Вторая 🐍')
btnSamPython3 = KeyboardButton('Третья 🐍')
SamPythonMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnSamPython1, btnSamPython2, btnSamPython3, btnBack)

btnSamPascal1 = KeyboardButton('Первая 🔤')
btnSamPascal2 = KeyboardButton('Вторая 🔤')
btnSamPascal3 = KeyboardButton('Третья 🔤')
SamPascalMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnSamPascal1, btnSamPascal2, btnSamPascal3, btnBack)

lanHelpMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnBack)

