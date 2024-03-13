import asyncio
from aiogram import Bot, Dispatcher

from config import TOKEN_API
from app.handlers import router

#оголошення змінних
bot = Bot(token=TOKEN_API, parse_mode='HTML')
dp = Dispatcher()


#запуск
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
