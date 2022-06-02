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

btnSamCs1 = KeyboardButton('Условия C#')
btnSamCs2 = KeyboardButton('Циклы C#')
btnSamCs3 = KeyboardButton('Массивы C#')
SamCsMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnSamCs1, btnSamCs2, btnSamCs3, btnBack)

btnSamPython1 = KeyboardButton('Условия 🐍')
btnSamPython2 = KeyboardButton('Циклы 🐍')
btnSamPython3 = KeyboardButton('Массивы 🐍')
SamPythonMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnSamPython1, btnSamPython2, btnSamPython3, btnBack)

btnSamPascal1 = KeyboardButton('Первая 🔤')
btnSamPascal2 = KeyboardButton('Вторая 🔤')
btnSamPascal3 = KeyboardButton('Третья 🔤')
SamPascalMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnSamPascal1, btnSamPascal2, btnSamPascal3, btnBack)

lanHelpMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnBack)

btnIfElseCs = KeyboardButton("Оператор If Else C#")
btnSwitchCs = KeyboardButton("Оператор Switch C#")

btnWhileCs = KeyboardButton("Оператор while C#")
btnWhileDoCs = KeyboardButton("Оператор do while C#")
btnForCs = KeyboardButton("Оператор for C#")

btnMakeCs = KeyboardButton("Обьявление массива C#")
btnInitCs = KeyboardButton("Инициализация массива C#")
btnSortCs = KeyboardButton("Пример сортировки C#")

UslCsMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnIfElseCs, btnSwitchCs, btnBack)
CycleCsMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnWhileCs, btnWhileDoCs, btnForCs, btnBack)
MasCsMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnMakeCs, btnInitCs, btnSortCs, btnBack)

btnIfPy = KeyboardButton("Конструкция if 🐍")
btnIfElsePy = KeyboardButton("Конструкция if - else 🐍")
btnIfElifPy = KeyboardButton("Конструкция if - elif - else 🐍")

btnForPy = KeyboardButton("Оператор for 🐍")
btnWhilePy = KeyboardButton("Оператор while 🐍")
btnBreakConPy = KeyboardButton("Операторы break и continue 🐍")

btnCreateMasPy = KeyboardButton("Создание массива 🐍")
btnPyMasMethods = KeyboardButton("Методы массивов 🐍")
btnPyObhodMas = KeyboardButton("Обход массивов 🐍")

UslPyMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnIfPy, btnIfElsePy, btnIfElifPy, btnBack)
CyclePyMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnForPy, btnWhilePy, btnBreakConPy, btnBack)
MasPyMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnCreateMasPy, btnPyMasMethods, btnPyObhodMas, btnBack)
