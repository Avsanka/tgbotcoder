from aiogram import types
from aiogram.types import ContentTypes, Message

import bot
from dispatcher import dp
import config
import markup as nav
import dicts as dic

async def photo_answer(message: Message, photo_file_id):
    s = dic.dictSam[message.text]
    await message.reply(s, reply_markup=nav.samMenu)
    await dp.bot.send_photo(chat_id=message.from_user.id, photo=photo_file_id)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Привет!\n Я бот-кодер, помощник программиста\n Я помогу тебе научиться программировать", reply_markup=nav.mainMenu)

@dp.message_handler(content_types=ContentTypes.PHOTO)
async def send_photo(message: Message):
    await message.reply(message.photo[-1].file_id)



#------условия-------#
@dp.message_handler(text='Оператор If Else C#')
async def answer(message: Message):
    photo_file_id = 'AgACAgIAAxkBAAIIjWKXqdM-CWEtzBcUBZQiNXWreBsHAALJvDEbIEzBSCEhsLPCE-a0AQADAgADeAADJAQ'
    await photo_answer(message, photo_file_id)

@dp.message_handler(text='Оператор Switch C#')
async def answer(message: Message):
    photo_file_id = 'AgACAgIAAxkBAAIIi2KXqdDJ8UAWCqxG-at_kKP-MLwgAALIvDEbIEzBSPNNe6wi5EQjAQADAgADeAADJAQ'
    await photo_answer(message, photo_file_id)

#------условия-------#

#------Циклы-------#

@dp.message_handler(text='Оператор while C#')
async def answer(message: Message):
    photo_file_id = 'AgACAgIAAxkBAAIIpWKXqyVQoM8foET-w0oIeLnu0XNkAALPvDEbIEzBSN6nhKP9rWXyAQADAgADbQADJAQ'
    await photo_answer(message, photo_file_id)

@dp.message_handler(text='Оператор do while C#')
async def answer(message: Message):
    photo_file_id = 'AgACAgIAAxkBAAIIp2KXqygDvvooH7aMdNWDWLJN7Cq7AALQvDEbIEzBSN0t-lFLestpAQADAgADbQADJAQ'
    await photo_answer(message, photo_file_id)

@dp.message_handler(text='Оператор for C#')
async def answer(message: Message):
    photo_file_id = 'AgACAgIAAxkBAAIIqWKXqyvKQpd8ElcWJH8IcEHjCEYcAALRvDEbIEzBSK-UJbrP1o30AQADAgADeAADJAQ'
    await photo_answer(message, photo_file_id)

#------Циклы-------#

#------Массивы-------#
@dp.message_handler(text='Обьявление массива C#')
async def answer(message: Message):
    photo_file_id = 'AgACAgIAAxkBAAIJmGKXr4vJoBABqfgEmQNHdK10RWSpAALmvDEbIEzBSOoJPeHbllKfAQADAgADeAADJAQ'
    await photo_answer(message, photo_file_id)

@dp.message_handler(text='Инициализация массива C#')
async def answer(message: Message):
    photo_file_id = 'AgACAgIAAxkBAAIJmmKXr40GTCRbYBPmsJbsMmbVNCCGAALnvDEbIEzBSPXh5E-508ckAQADAgADeAADJAQ'
    await photo_answer(message, photo_file_id)

@dp.message_handler(text='Пример сортировки C#')
async def answer(message: Message):
    photo_file_id = 'AgACAgIAAxkBAAIJnGKXr4_gTt05EDraFeHs3JigVSivAALovDEbIEzBSCdmfr1-3XFrAQADAgADeAADJAQ'
    await photo_answer(message, photo_file_id)

#------Массивы-------#

#python

#------условия-------#
@dp.message_handler(text='Конструкция if 🐍')
async def answer(message: Message):
    photo_file_id = 'AgACAgIAAxkBAAIKLWKXt5IREtQy94muNXP_OSy7jTXVAAIsvTEbIEzBSI-bA5BZ3tAkAQADAgADeAADJAQ'
    await photo_answer(message, photo_file_id)

@dp.message_handler(text='Конструкция if - else 🐍')
async def answer(message: Message):
    photo_file_id = 'AgACAgIAAxkBAAIKL2KXt5WPPzyiHGJJ5BXvjEwV1OHPAAItvTEbIEzBSKSZHjxCx58QAQADAgADeAADJAQ'
    await photo_answer(message, photo_file_id)

@dp.message_handler(text='Конструкция if - elif - else 🐍')
async def answer(message: Message):
    photo_file_id = 'AgACAgIAAxkBAAIKMWKXt5j0xOx42sownXv3s9kkGlPHAAIuvTEbIEzBSEPIXILW4A0jAQADAgADeAADJAQ'
    await photo_answer(message, photo_file_id)

#------условия-------#

#------Циклы-------#
@dp.message_handler(text='Оператор for 🐍')
async def answer(message: Message):
    photo_file_id = 'AgACAgIAAxkBAAIKX2KXulBEAAHYLIDMZkELYpjiwGt3CAACML0xGyBMwUgLjjqfXmNZpgEAAwIAA3gAAyQE'
    await photo_answer(message, photo_file_id)

@dp.message_handler(text='Оператор while 🐍')
async def answer(message: Message):
    photo_file_id = 'AgACAgIAAxkBAAIKYWKXulP-YdjFgeH88dffvaW4rYMoAAIxvTEbIEzBSMzHLaK8KWD8AQADAgADbQADJAQ'
    await photo_answer(message, photo_file_id)

@dp.message_handler(text='Операторы break и continue 🐍')
async def answer(message: Message):
    s = dic.dictSam[message.text]
    await message.reply(s, reply_markup=nav.samMenu)
#------Циклы-------#

#------Массивы-------#
@dp.message_handler(text='Создание массива 🐍')
async def answer(message: Message):
    photo_file_id = 'AgACAgIAAxkBAAIK6mKXvTVxp0NjFfiGEpL8g74nMvoKAAI5vTEbIEzBSHjHwa81ZDOaAQADAgADeAADJAQ'
    await photo_answer(message, photo_file_id)

@dp.message_handler(text='Методы массивов 🐍')
async def answer(message: Message):
    photo_file_id = 'AgACAgIAAxkBAAIK7GKXvTk-d9yTbwAB0cHKO6E63cZDCwACOr0xGyBMwUinp4Ax8i9fcQEAAwIAA3gAAyQE'
    await photo_answer(message, photo_file_id)

@dp.message_handler(text='Обход массивов 🐍')
async def answer(message: Message):
    photo_file_id = 'AgACAgIAAxkBAAIK7mKXvTygPWODWeVdXU1dRVjuuHa8AAI7vTEbIEzBSNvFaJEWtoFsAQADAgADbQADJAQ'
    await photo_answer(message, photo_file_id)


#------Массивы-------#

@dp.message_handler()
async def bot_message(message: types.Message):
    #---------------------------#

    if message.text == '📚ЕГЭ':
        await message.reply("Выбери действие", reply_markup=nav.egeLanMenu)

    elif message.text == '🔤Pascal':
        await message.reply("пока в разработке", reply_markup=nav.egeLanMenu)

    elif message.text == '🐍Python':
        await message.reply("пока в разработке", reply_markup=nav.egeLanMenu)

    elif message.text == '➕C++':
        await message.reply("пока в разработке", reply_markup=nav.egeLanMenu)
    #--------------------------#

    #--------------------------#
    elif message.text == '🤓 Самостоятельное изучение':
        await message.reply("Выберите язык", reply_markup=nav.samMenu)

    elif message.text == '#️⃣C#':
        await message.reply("Выберите задачу", reply_markup=nav.SamCsMenu)

    elif message.text == '🐍Pythоn':
        await message.reply("Выберите задачу", reply_markup=nav.SamPythonMenu)

    elif message.text == '🔤Pascаl':
        await message.reply("Выберите задачу", reply_markup=nav.SamPascalMenu)
    #--------------------------#

    elif message.text == '✅Помощь с выбором языка':
        await message.reply("Пока в разработке", reply_markup=nav.lanHelpMenu)

    elif message.text == '⏮В главное меню':
        await message.reply("Вот главное меню", reply_markup=nav.mainMenu)

#-------------------------------After menu-----------------------------------------------#
    elif message.text == "Условия C#":
        await message.reply("Условные операторы – это конструкции, позволяющие управлять ходом выполнения программы в зависимости от определенных условий. В языке C# присутствует два типа таких конструкций: if - else и switch.", reply_markup=nav.UslCsMenu)

    elif message.text == "Циклы C#":
        await  message.reply("Циклы в языках программирования предназначены для построения конструкции, выполняющей заданный блок кода некоторое количество раз, которое определяется тем или иным условием. C# предоставляет три разных варианта построения циклов.", reply_markup=nav.CycleCsMenu)

    elif message.text == "Массивы C#":
        await message.reply("Массив – это объединенная в единое целое группа переменных одного типа к которым можно обращаться по единому имени. Доступ к элементам одномерного массива осуществляется с помощью индекса, который определяет их положение. Индексация массивов начинается с нуля. Чтобы получить доступ к элементу массива с помощью индекса, нужно взять индекс элемента в квадратные скобки.", reply_markup=nav.MasCsMenu)




    elif message.text == "Условия 🐍":
        await message.reply("Условные операторы – это конструкции, позволяющие управлять ходом выполнения программы в зависимости от определенных условий. Я могу рассказать о конструкциях if, if-else и if-elif-else", reply_markup=nav.UslPyMenu)

    elif message.text == "Циклы 🐍":
        await message.reply("Циклы в языках программирования предназначены для построения конструкции, выполняющей заданный блок кода некоторое количество раз, которое определяется тем или иным условием. В Python, как и во многих других языках есть 2 вида циклов: for и while", reply_markup=nav.CyclePyMenu)

    elif message.text == "Массивы 🐍":
        await message.reply("Массив – это объединенная в единое целое группа переменных одного типа к которым можно обращаться по единому имени. Доступ к элементам одномерного массива осуществляется с помощью индекса, который определяет их положение. Важно не забывать, что индексация массива начинается с нуля", reply_markup=nav.MasPyMenu)





