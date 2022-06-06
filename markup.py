from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnBack = KeyboardButton('⏮В главное меню')
btnSamBack = KeyboardButton("⏮Назад")

btnMainEge = KeyboardButton('📚Основные термины')
btnMainSam = KeyboardButton('🤓 Самостоятельное изучение')
btnMainLanHelp = KeyboardButton('✅Помощь с выбором языка')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(btnMainEge, btnMainSam, btnMainLanHelp)

btnMainTerms = KeyboardButton('📚Базовые термины')
btnHardTerms = KeyboardButton('📚Продвинутые термины')
btnTypes = KeyboardButton('📚Типы данных')
termsMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnMainTerms, btnHardTerms, btnTypes, btnBack)

btnSamCs = KeyboardButton('#️⃣C#')
btnSamPython = KeyboardButton('🐍Pythоn')
btnSamPascal = KeyboardButton('🔤Pascаl')
samMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnSamCs, btnSamPython, btnSamPascal, btnBack)

btnSamCs1 = KeyboardButton('Условия C#')
btnSamCs2 = KeyboardButton('Циклы C#')
btnSamCs3 = KeyboardButton('Массивы C#')
SamCsMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnSamCs1, btnSamCs2, btnSamCs3, btnSamBack)

btnSamPython1 = KeyboardButton('Условия 🐍')
btnSamPython2 = KeyboardButton('Циклы 🐍')
btnSamPython3 = KeyboardButton('Массивы 🐍')
SamPythonMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnSamPython1, btnSamPython2, btnSamPython3, btnSamBack)

btnSamPascal1 = KeyboardButton('Циклы 🔤')
btnSamPascal2 = KeyboardButton('Условия 🔤')
btnSamPascal3 = KeyboardButton('Массивы 🔤')
SamPascalMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnSamPascal1, btnSamPascal2, btnSamPascal3, btnSamBack)

lanHelpMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnBack)

btnIfElseCs = KeyboardButton("Оператор If Else C#")
btnSwitchCs = KeyboardButton("Оператор Switch C#")

btnWhileCs = KeyboardButton("Оператор while C#")
btnWhileDoCs = KeyboardButton("Оператор do while C#")
btnForCs = KeyboardButton("Оператор for C#")

btnMakeCs = KeyboardButton("Обьявление массива C#")
btnInitCs = KeyboardButton("Инициализация массива C#")
btnSortCs = KeyboardButton("Пример сортировки C#")

UslCsMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnIfElseCs, btnSwitchCs, btnSamBack)
CycleCsMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnWhileCs, btnWhileDoCs, btnForCs, btnSamBack)
MasCsMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnMakeCs, btnInitCs, btnSortCs, btnSamBack)

btnIfPy = KeyboardButton("Конструкция if 🐍")
btnIfElsePy = KeyboardButton("Конструкция if - else 🐍")
btnIfElifPy = KeyboardButton("Конструкция if - elif - else 🐍")

btnForPy = KeyboardButton("Оператор for 🐍")
btnWhilePy = KeyboardButton("Оператор while 🐍")
btnBreakConPy = KeyboardButton("Операторы break и continue 🐍")

btnCreateMasPy = KeyboardButton("Создание массива 🐍")
btnPyMasMethods = KeyboardButton("Методы массивов 🐍")
btnPyObhodMas = KeyboardButton("Обход массивов 🐍")

UslPyMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnIfPy, btnIfElsePy, btnIfElifPy, btnSamBack)
CyclePyMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnForPy, btnWhilePy, btnBreakConPy, btnSamBack)
MasPyMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnCreateMasPy, btnPyMasMethods, btnPyObhodMas, btnSamBack)

btnForPas = KeyboardButton("Оператор for 🔤")
btnWhilePas = KeyboardButton("Оператор while 🔤")
btnRepPas = KeyboardButton("Оператор repeat 🔤")

btnIfElsePas = KeyboardButton("Конструкция if-else 🔤")
btnIfPas = KeyboardButton("Конструкция только с if 🔤")
btnOtherPas = KeyboardButton("Операторы then, begin, end 🔤")

btnWhyPas = KeyboardButton("Зачем нужен массив? 🔤")
btnMakeMasPas = KeyboardButton("Как объявить массив? 🔤")
btnMasInitPas = KeyboardButton("Чтение и запись в массив 🔤")

CyclePasMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnForPas, btnWhilePas, btnRepPas, btnSamBack)
UslPasMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnIfElsePas, btnIfPas, btnOtherPas, btnSamBack)
MasPasMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnWhyPas, btnMakeMasPas, btnMasInitPas, btnSamBack)

btnYes = KeyboardButton("Да")
btnSoso = KeyboardButton("Немного")
btnNo = KeyboardButton("Нет")
q1 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnYes, btnSoso, btnNo)

btnYes2 = KeyboardButton("Дa")
btnNo2 = KeyboardButton("Нeт")
btnTried = KeyboardButton("Пытался")
q2 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnYes2, btnTried, btnNo2)

btnHard = KeyboardButton("Сложный")
btnEasy = KeyboardButton("Что-то между")
btnMiddle = KeyboardButton("Простой")
q3 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnHard, btnMiddle, btnEasy)

btnWork = KeyboardButton("Для работы")
btnStudy = KeyboardButton("Для учёбы")
btnProst = KeyboardButton("Личный интерес")
q4 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnWork, btnStudy, btnProst)

btnHigh = KeyboardButton("Высшее")
btnMid = KeyboardButton("Среднее")
btnOther = KeyboardButton("Другое")
q5 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnHigh, btnMid, btnOther)
