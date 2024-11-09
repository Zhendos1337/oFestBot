import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from app.main_menu import router
from app.quests import router as r1
from app.squads_about import router as r2
from app.admins import router as r3
from app.special import router as r4

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(router, r1, r2, r3, r4)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except:
            print('Exit')


