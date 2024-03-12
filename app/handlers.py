import random
import config
from aiogram.enums import ParseMode
from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from config import SPECIAL_USER_ID, SPECWORD
import app.keyboard as kb
import app.functions as func

router = Router()

#статуси для діапазону чисел
class Choose(StatesGroup):
    numone = State()
    numtwo = State()

#статус для кнопок діапазону
class Count(StatesGroup):
    count = State()

#команда старт
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привіт,{message.from_user.first_name}, я бот-рандомайзер!',
                         reply_markup=kb.main)
    await message.answer(f'\nЯ можу кидати гральні куби стандартних видів,'
                         f' для цього натисни кнопку "Куби".'
                         '\nСпробуй /help для отримання списку команд.',
                         reply_markup=kb.startmesskb)


###особисте привітання
@router.message(F.text == 'привет')
async def special_answer(message: Message):
    if (message.from_user.id == config.SPECIAL_USER_ID):
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

##крінж
@router.message(F.text == 'задание')
async def task_message(message: Message):
    await message.answer(f'{config.SPECWORD} {func.list_choose(func.listin)}')


#Кнопки основної клавіатури

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
async def choosenum(message: Message, state: FSMContext):
#    await state.clear()
#    data = await state.update_data(numone='0', numtwo='1')
#    print(data["numone"],data["numtwo"])
    await state.set_state(Choose.numone)
    await message.answer(f'Введіть з якого числа починається діапазон для вибору:')
###Крок перший вибір першого числа
@router.message(Choose.numone)
async def choosenumone(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(numone=message.text)
        data = await state.get_data()
        await state.set_state(Choose.numtwo)
        await message.answer(f'Введіть до якого числа йде діапазон:')
    else:
        if message.text == 'хуй':
            await message.answer(f'Сам ти хуй!')
        await message.answer(f'Ви ввели не число!')

###крок другий вибір кінцевого числа діапазону
@router.message(Choose.numtwo)
async def choosenumtwo(message: Message, state: FSMContext, c1 = 1):
    if message.text.isdigit():
        await state.update_data(numtwo=message.text)
        data = await state.get_data()
        a = data["numone"]
        b = data["numtwo"]
        await message.answer(f'Ваш діапазон від {data["numone"]} до {data["numtwo"]}.'
                             f'Кількість чисел які будуть вибрані: {c1}'
                             f'Без повторів: ',
                             ##кнокпки не работают возникает ошибка
                             reply_markup=kb.choosenumkb)
        ##зробити коротше
        a1 = func.min_num(a, b)
        b1 = func.max_num(a, b)
        a2 = int(a1)
        b2 = int(b1)
        await message.answer(f'\nРандомне число з діапазону: {random.randint(a2, b2)}')

    else:
        if message.text == 'хуй':
            await message.answer(f'Сам ти хуй!')
        await message.answer(f'Ви ввели не число!')

##тут возникает ошибка я потом исправлю
 #"Показати числа" під діапазоном
"""@router.callback_query(F.data == 'shownum')
async def shownum(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    a1 = int(a)
    b1 = int(b)
    print(a1, b1, type(a1),type(b1))
    a1 = func.min_num(a, b)
    b1 = func.max_num(a, b)
    a2 = int(a1)
    b2 = int(b1)"""


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


