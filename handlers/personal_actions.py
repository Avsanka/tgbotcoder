from aiogram import types
from dispatcher import dp
import config
import markup as nav
import dicts as dic

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Привет!\n Я бот-кодер, помощник программиста\n Я помогу тебе научиться программировать", reply_markup=nav.mainMenu)

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

    elif message.text == "Первая C#" or "Вторая C#" or "Третья C#" or "Первая 🐍" or "Вторая 🐍" or "Третья 🐍"\
            "Первая 🔤" or "Вторая 🔤" or "Третья 🔤":
        s = dic.dictSam[message.text]
        await message.reply(s, reply_markup=nav.samMenu)




