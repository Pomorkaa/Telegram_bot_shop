#убрать маты, сделать модерацию матов. в файле со списком матов между ними пустая строка. функцию ниже в отдельном файле 
#сохраняем и в файл джсон уже в папку пректа запихиваем
import json
# from create_bot import dp
from aiogram import Dispatcher, types
import string

# ar = []
# #
# with open('mtg_shop/mat.txt', encoding='utf-8') as r:
#     for i in r:
#         n = i.lower().split('\n')[0]
#         if n != '':
#             ar.append(n)

# with open('mat.json', 'w', encoding='utf-8') as fp:
#     json.dump(ar, fp)

#                 #функция дамп позволяет записать данные в json файл
# print(ar)
#сама функция убирания мата ниже. она должна быть обязательно под всеми хандлерами где есть параметры:

#
#
#
# @dp.message_handler()
async def check_cenz(message: types.Message):
    if {i.lower().translate(str.maketrans("","", string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open("mtg_shop/mat.json")))) != set():
        await message.reply('Маты запрещены!')
        await message.delete()


def register_handler_check(dp: Dispatcher):
    dp.register_message_handler(check_cenz)






# '''--------------------------------КЛАВИАТУРА-------------------------------------'''

