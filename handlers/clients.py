from aiogram import types, Dispatcher, bot
from create_bot import dp, bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from sqlite_db import sglite_db



# '''--------------------------------КЛАВИАТУРА-------------------------------------'''

b1=KeyboardButton('/start')
b2=KeyboardButton('/help')
b3=KeyboardButton('/Режим_работы')
b4=KeyboardButton('/Расположение')
b5=KeyboardButton('/Меню')
# b6=KeyboardButton('/Поделиться номером',request_contact=True)
# b7=KeyboardButton('/Отправить где я',request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b5).add(b3).add(b4).add(b2)


# '''--------------------------------ОСТАЛЬНОЕ-------------------------------------'''
# @dp.message_handler(commands=['start','help'])
async def command_start(message: types.Message):
    # try:
    await bot.send_message(message.from_user.id,'Добрый день!', reply_markup = kb_client)
    await message.delete()
    # except:
    #     await message.reply('Общение с ботом через ЛСб напишите ему : \nhttps://t.me/Pomorkaa_bot')

# @dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(user_id,'Пн-Пт с 9:00-20:00\nСб-Вс с 10:00-21:00')

# @dp.message_handler(commands=['Расположение']) 
async def pizza_adres_command(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(user_id,'Г. Расколлбасный ул. Беконная 26')

# @dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
    await sglite_db.sql_read(message)


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands= ['start','help'])
    dp.register_message_handler(pizza_open_command, commands= ['Режим_работы'])
    dp.register_message_handler(pizza_adres_command, commands= ['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands = ['Меню'])


