#Перша версія бота
import asyncio
import random
from config import TOKEN_API
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

#оголошення змінних
bot = Bot(TOKEN_API)
dp = Dispatcher()

#команда старт
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привіт, я бот-рандомайзер!'
                         '\nПоки що я нічого не вмію, але це лише перший етап.'
                         '\nСпробуй /help для отримання списку команд.')

#команда хелп
@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer("Список доступних команд: \n"
                         "/start \n/help "
                         "\nНажаль поки що немає інших команд(( ")

#пасхалка
@dp.message(F.text=='пасхалка')
async def rickroll_message(message: Message):
    await message.answer('Never gonna give you up!')
    await message.answer('Never gonna let you down!')
    await message.answer('Never gonna run around and desert you!')

#запуск
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
