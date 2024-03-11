import random
from aiogram.enums import ParseMode
from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode
from middlewares import NumChooseMiddleware

import app.keyboard as kb

router = Router()



#команда старт
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привіт,{message.from_user.first_name}, я бот-рандомайзер!',
                         reply_markup=kb.main)
    await message.answer(f'\nПоки що я нічого не вмію, але це лише перший етап.'
                         '\nСпробуй /help для отримання списку команд.',
                         reply_markup=kb.startmesskb)



@router.message(F.text == 'привет')
async def special_answer(message: Message):
    if (message.from_user.id == 842172831):
        await message.reply('Привет Паркет!')


#команда хелп
@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer("Список доступних команд: \n"
                         "/start \n/help "
                         "\nНажаль поки що немає інших команд(( ")

#пасхалка
@router.message(F.text=='пасхалка')
async def rickroll_message(message: Message):
    await message.answer('<tg-spoiler>Never gonna give you up!</tg-spoiler>')
    await message.answer('<tg-spoiler>Never gonna let you down!</tg-spoiler>')
    await message.answer('<tg-spoiler>Never gonna run around and desert you!</tg-spoiler>')

#Кнопки

##Кубики
@router.message(F.text == 'Куби')
async def cube_message(message: Message):
    await message.answer(f'Обери кубик який хочеш кинути:',
                         reply_markup=await kb.inline_cubes())
###Куб 4 сторони
@router.callback_query(F.data == 'cube_D4')
async def cube_D4(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(f'Ви кинули куб з 4 сторонами, вам випало: {random.randint(1,4)}\n'
                                     f'Бажаєте кинути ще раз:',
                                     reply_markup=await kb.inline_cubes())
###Куб 6 сторін
@router.callback_query(F.data == 'cube_D6')
async def cube_D6(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(f'Ви кинули куб з 6 сторонами, вам випало: {random.randint(1,6)}\n'
                                     f'Бажаєте кинути ще раз:',
                                     reply_markup=await kb.inline_cubes())
###Куб 8 сторін
@router.callback_query(F.data == 'cube_D8')
async def cube_D8(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(f'Ви кинули куб з 8 сторонами, вам випало: {random.randint(1,8)}\n'
                                     f'Бажаєте кинути ще раз:',
                                     reply_markup=await kb.inline_cubes())
###Куб 10 сторін
@router.callback_query(F.data == 'cube_D10')
async def cube_D10(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(f'Ви кинули куб з 10 сторонами, вам випало: {random.randint(1,10)}\n'
                                     f'Бажаєте кинути ще раз:',
                                     reply_markup=await kb.inline_cubes())
###Куб 12 сторін
@router.callback_query(F.data == 'cube_D12')
async def cube_D12(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(f'Ви кинули куб з 12 сторонами, вам випало: {random.randint(1,12)}\n'
                                     f'Бажаєте кинути ще раз:',
                                     reply_markup=await kb.inline_cubes())
###Куб 20 сторін
@router.callback_query(F.data == 'cube_D20')
async def cube_D20(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(f'Ви кинули куб з 20 сторонами, вам випало: {random.randint(1,20)}\n'
                                     f'Бажаєте кинути ще раз:',
                                     reply_markup=await kb.inline_cubes())

##Число з діапазона
@router.message(F.text == 'Обрати число')
async def cube_message(message: Message):
    await message.answer(f'Введи діапазон чисел:')





#ехо
"""@router.message()
async def echo_handler(message: types.Message):
    try:
        # повернення повідомлень
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # я не знаю навіщо але нехай буде
        await message.answer("Nice try!")"""

#ще одна пасхала аято&итто


