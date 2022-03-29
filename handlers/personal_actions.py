from aiogram import types
from dispatcher import dp
import config
import markup as nav

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Привет!\n Я бот-кодер, помощник программиста\n но пока что я только повторюшка", reply_markup=nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'ЕГЭ':
        await  message.reply("Выбери действие", reply_markup=nav.egeLanMenu)

    elif message.text == 'Самостоятельное изучение':
        await  message.reply("Выберите язык", reply_markup=nav.samMenu)

    elif message.text == 'Помощь с выбором языка':
        await  message.reply("Пока в разработке", reply_markup=nav.lanHelpMenu)
        
    elif message.text == 'C++':
        await  message.reply("пока в разработке", reply_markup=nav.samMenu)

    elif message.text == 'Back to main':
        await message.reply("Вот главное меню", reply_markup=nav.mainMenu)




