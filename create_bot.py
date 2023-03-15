from aiogram import Bot, Dispatcher
from aiogram.types import ReplyKeyboardMarkup
import logging
from KEY_ALL import TG_key
# import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage # сохранит в файле. 
#Если хранить надо пароли и тд, и чтоб стопудов все сохранилось то нужна база данных, редис и тд

storage = MemoryStorage()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TG_key)
# bot = Bot(token = os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())



