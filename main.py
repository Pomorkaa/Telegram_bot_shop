
from aiogram import executor
from create_bot import dp
from sqlite_db import sglite_db

async def on_startup(_):
    print('Бот вышел в онлайн')  
    sglite_db.sql_start()

 

from handlers import clients,admin,check

clients.register_handler_client(dp)
admin.register_hanglers_admin(dp)
check.register_handler_check(dp)


#запустить бот
if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True,on_startup=on_startup)
