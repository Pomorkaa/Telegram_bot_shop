from aiogram.dispatcher import FSMContext # указываем что это из дисп состояний
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from create_bot import bot, dp
from sqlite_db import sglite_db
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton , InlineKeyboardButton, InlineKeyboardMarkup


ID = None

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

but_load = KeyboardButton('/Загрузить')
but_delete = KeyboardButton('/Удалить')

but_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(but_load).add(but_delete)

#получаем айди текущего модератора
# @dp.message_handler(commands=['Модератор'], is_chat_admin=True )
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id,'Что хозяин надо?', reply_markup=but_case_admin)
    await message.delete()

# @dp.message_handler(commands='Загрузить',state=None)
async def cm_start(message: types.Message):
    if ID == message.from_user.id:
        await FSMAdmin.photo.set()
        await message.reply('Загрузи фото')
    else:
        await message.reply('кажись доступ запрещен лезь в админку')

# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state=FSMContext):
    if ID == message.from_user.id:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Теперь введи название')


# @dp.message_handler(state=FSMContext)
async def load_name(message: types.Message, state=FSMContext):
    if ID == message.from_user.id:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Введи описание')

# @dp.message_handler(state=FSMAdmin.descripton)
async def load_description(message: types.Message, state=FSMContext):
    if ID == message.from_user.id:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Введи цену')



# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state=FSMContext):
    if ID == message.from_user.id:
        async with state.proxy() as data:
            data['price'] = float(message.text)
    
        # async with state.proxy() as data:
        #     await message.reply(str(data))
        await sglite_db.sql_add_command(state)
        await state.finish()  #бот выйдет из машины состоянит и удалит все что вы записали

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sglite_db.sql_delete_command(callback_query.data.replace('del ',''))
    await callback_query.answer(text = "{} удалена".format(callback_query.data.replace('del ','')) , show_alert=True)



@dp.message_handler(commands='Удалить')
async def del_item(message: types.Message):
    if ID == message.from_user.id:
        read = await sglite_db.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\n Цена: {ret[-1]}')
            await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data= f'del {ret[1]}')))



            # await callback_query.answer(text = f'{callback_query.data.replace('del ', "")} удалена', show_alert = True)

    
# @dp.message_handler(state="*", commands='отмена')
# @dp.message_handler(Text(equals='отмена',ignore_case=True)state="*")
async def cansel_handler(message: types.Message, state= FSMContext):
    if ID == message.from_user.id:
    
        current_state = await state.get_state()             #получаем состояние
        if current_state is None:                           #проверяем состояние
            return
        await state.finish()
        await message.reply('ОК, отменили котик, подумай еще')


def register_hanglers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands='Загрузить', state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price,state=FSMAdmin.price)
    dp.register_message_handler(cansel_handler,state="*", commands='отмена')
    dp.register_message_handler(cansel_handler, Text(equals='отмена',ignore_case=True), 
    state="*")
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)

  








