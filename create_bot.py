from aiogram import Bot, Dispatcher
from aiogram.types import ReplyKeyboardMarkup
import logging
# import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage # сохранит в файле. 
#Если хранить надо пароли и тд, и чтоб стопудов все сохранилось то нужна база данных, редис и тд

storage = MemoryStorage()

logging.basicConfig(level=logging.INFO)
bot = Bot(token="6128302810:AAFBv5UNfWP0qTPD4ZuvASDN_CujOru-C_I")
# bot = Bot(token = os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())



