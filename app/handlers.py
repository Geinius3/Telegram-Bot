import random
import config
from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import app.keyboard as kb
import app.functions as func
from sqlite import botdb
BotDB = botdb("D:/SQLite/usersqlite.db")


router = Router()

#статус для кнопок діапазону
class Count(StatesGroup):
    count = State()

#статуси для діапазону чисел
class Choose(StatesGroup):
    numone = State()
    numtwo = State()


#статус для кнопок діапазону
class Listchooser(StatesGroup):
    listchooser = State()

#команда старт
@router.message(CommandStart())
async def cmd_start(message: Message):
    """Додання користувача до бд """
    if(not BotDB.user_exists(user_id=message.from_user.id)):
        BotDB.add_user(user_id=message.from_user.id)
    BotDB.update_restate(user_id=message.from_user.id, restate=False)
    BotDB.update_actionstate(user_id=message.from_user.id, actionstate=0)
    BotDB.update_list(user_id=message.from_user.id, list='')
    await message.answer(f'Привіт,{message.from_user.first_name}, я бот-рандомайзер!',
                         reply_markup=kb.main)
    await message.answer(f'\nЯ можу кидати гральні куби стандартних видів,'
                         f" обирати випадкове число чи об'єкт за вказаними умовами"
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
    await message.answer("Тут ви можете отримати інформацію про необхідну команду "
                         "чи функцію, для цього натисніть на кнопку під повідомленням. \n"
                         "\nНажаль поки що немає інших команд(( ",
                         reply_markup= kb.helplist)

##Кнопка інфо про старт
@router.callback_query(F.data == 'startinfo')
async def startinfo(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(f'Інформація про команди\n'
                                     f'/start - команда початку роботи з ботом,'
                                     f' у відповідь ви отримаєте коротко інформацію про бота'
                                     f' і важливе посилання)',
                                     reply_markup= kb.helplist)

##Кнопка інфо про хелп
@router.callback_query(F.data == 'helpinfo')
async def helpinfo(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(f'Інформація про команди\n'
                                     f'/help - команда допомоги, з неї ви дізнаєтесь'
                                     f' опис та особливості роботи команд та функцій боту'
                                     f'\n(Ви зараз її використовуєте))',
                                     reply_markup= kb.helplist)

##Кнопка інфо про рандом стікер
@router.callback_query(F.data == 'randstickinfo')
async def randstickinfo(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(f'Інформація про команди\n'
                                     f'/randomsticker - команда визову рандомного стікера.'
                                     f' Все просто, ви натискаєте команду - бот присилає випадковий стікер'
                                     f'\nЦе весело, тому спробуйте(b ᵔ▽ᵔ)b ',
                                     reply_markup= kb.helplist)


#Чергова весела фіча
@router.message(Command('randomsticker'))
async def randomsticker(message: Message):
    await message.answer_sticker(func.rand_stick(config.STICKER_LIST))




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

##Вибір зі списку
@router.message(F.text == 'Вибрати зі списку')
async def listobject(message: Message, state: FSMContext):
    await state.set_state(Listchooser.listchooser)
    await message.answer(f"Введіть список об'єктів для вибору випадкового:\n"
                         f"Задайте список у вигляді\n"
                         f"[Перший об'єкт],[Другий об'єкт],[Третій об'єкт]")

###Виконання функціі і рандомізаія об"єкту
@router.message(Listchooser.listchooser)
async def listobjchoose(message: Message, state: FSMContext):
    BotDB.update_actionstate(message.from_user.id, actionstate=2)
    await state.update_data(listchooser=message.text)
    data = await state.get_data()
    await state.clear()
    a = data["listchooser"]
    BotDB.update_list(message.from_user.id, list=a)
    listholder = func.list_to_mass(a)
    i = random.randint(0, len(listholder)-1)
    await message.answer(f"Випадковий об'єкт із заданого списку: {listholder[i]}")

##Число з діапазона
@router.message(F.text == 'Обрати число')
async def choosenum(message: Message, state: FSMContext):
    BotDB.update_numbercount(user_id=message.from_user.id, numbercount=1)
    BotDB.update_actionstate(user_id=message.from_user.id, actionstate=1)
    await state.set_state(Choose.numone)
    await message.answer(f'Введіть з якого числа починається діапазон для вибору:')
###Крок перший вибір першого числа
@router.message(Choose.numone)
async def choosenumone(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(numone=message.text)
        data = await state.get_data()
        numa_fordb = int(data["numone"])
        BotDB.update_datanuma(datanumber_a=numa_fordb, user_id=message.from_user.id)
        await state.set_state(Choose.numtwo)
        await message.answer(f'Введіть до якого числа йде діапазон:')
    else:
        if message.text == 'хуй':
            await message.answer(f'Сам ти хуй!')
        await message.answer(f'Ви ввели не число!')

###крок другий вибір кінцевого числа діапазону
@router.message(Choose.numtwo)
async def choosenumtwo(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(numtwo=message.text)
        data = await state.get_data()
        numb_fordb = int(data["numtwo"])
        BotDB.update_datanumb(datanumber_b=numb_fordb, user_id=message.from_user.id)
        c1 = BotDB.get_numbercount(user_id=message.from_user.id)
        c1 = int(c1[0])
        restate = BotDB.get_restate(user_id=message.from_user.id)
        restate = bool(restate[0])
        statestr = func.which_state(restate=restate)
        await message.answer(f'Ваш діапазон від {data["numone"]} до {data["numtwo"]}.'
                             f'\nКількість чисел які будуть вибрані: {c1}\n'
                             f'Без повторів: {statestr}',
                             ##кнокпки не работают возникает ошибка
                             reply_markup=kb.choosenumkb)

        await state.clear()
    else:
        if message.text == 'хуй':
            await message.answer(f'Сам ти хуй!')
        await message.answer(f'Ви ввели не число!')

###кнопка показати числа
@router.callback_query(F.data == 'shownum')
async def numbergenerate(callback: CallbackQuery):
    await callback.answer('')
    numa_fromdb = BotDB.get_datanuma(user_id=callback.from_user.id)
    numa_fromdb = int(numa_fromdb[0])
    numb_fromdb = BotDB.get_datanumb(user_id=callback.from_user.id)
    numb_fromdb = int(numb_fromdb[0])
    numcount_fromdb = BotDB.get_numbercount(user_id=callback.from_user.id)
    c1 = int(numcount_fromdb[0])
    restate = BotDB.get_restate(user_id=callback.from_user.id)
    restate = bool(restate[0])
    print(restate)
    a1 = func.min_num(numa_fromdb, numb_fromdb)
    b1 = func.max_num(numa_fromdb, numb_fromdb)
    if restate == False:
        result = str(func.numgenerate(a1, b1, c1))
        await callback.message.answer(f'\nРандомнi числa з діапазону: {result}')
    elif (restate == True) and (c1 <= (b1-a1+1)):
        result = str(func.numgenerateon(a1, b1, c1))
        await callback.message.answer(f'\nРандомнi числa з діапазону: {result}')
    else:
        await callback.message.answer('Умова неможлива! Кількість згенерованих чисел не може бути '
                              'більша за кількість можливих неповторюваних чисел! Вимкніть '
                              'функцію "Без повторів" або вкажіть меншу кількість чисел'
                              ' для генерації.')

##Кнопочка задати ількість чисел
@router.callback_query(F.data == 'countnums')
async def numbercount(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(Count.count)
    await callback.message.answer(f'Введіть кількість чисел що будуть згенеровані:')

###задати кількість встановлення кількості
@router.message(Count.count)
async def setnumcoun(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(count=message.text)
        data = await state.get_data()
        numcount_fordb = int(data["count"])
        BotDB.update_numbercount(user_id=message.from_user.id, numbercount=numcount_fordb)
        numcount_fromdb = BotDB.get_numbercount(user_id=message.from_user.id)
        c1 = int(numcount_fromdb[0])
        numa_fromdb = BotDB.get_datanuma(user_id=message.from_user.id)
        numa_fromdb = int(numa_fromdb[0])
        numb_fromdb = BotDB.get_datanumb(user_id=message.from_user.id)
        numb_fromdb = int(numb_fromdb[0])
        restate = BotDB.get_restate(user_id=message.from_user.id)
        restate = bool(restate[0])
        statestr = func.which_state(restate=restate)
        await message.answer(f'Ваш діапазон від {numa_fromdb} '
                               f'до {numb_fromdb}.'
                               f'\nКількість чисел які будуть вибрані: {c1}\n'
                               f'Без повторів: {statestr}',
                               reply_markup=kb.choosenumkb)
        await state.clear()

###без повторів
@router.callback_query(F.data == "repeatson")
async def repeatnums(callback: CallbackQuery):
    restate = BotDB.get_restate(user_id=callback.from_user.id)
    restate = bool(restate[0])
    restate = not restate
    BotDB.update_restate(user_id=callback.from_user.id, restate=restate)

    numa_fromdb = BotDB.get_datanuma(user_id=callback.from_user.id)
    numa_fromdb = int(numa_fromdb[0])
    numb_fromdb = BotDB.get_datanumb(user_id=callback.from_user.id)
    numb_fromdb = int(numb_fromdb[0])
    numcount_fromdb = BotDB.get_numbercount(user_id=callback.from_user.id)
    c1 = int(numcount_fromdb[0])
    statestr = func.which_state(restate=restate)
    await callback.message.edit_text(f'Ваш діапазон від {numa_fromdb} '
                               f'до {numb_fromdb}.'
                               f'\nКількість чисел які будуть вибрані: {c1}\n'
                               f'Без повторів: {statestr}',
                               reply_markup=kb.choosenumkb)



##Додати новий куб
@router.message(F.text == 'Додати куб')
async def addcube(message: Message):
    pass

##Повторити дію
@router.message(F.text == 'Повторити дію')
async def repeataction(message: Message):
    actionstate = BotDB.get_actionstate(message.from_user.id)
    actionstate = actionstate[0]
    if actionstate == 1:
        numa_fromdb = BotDB.get_datanuma(user_id=message.from_user.id)
        numa_fromdb = int(numa_fromdb[0])
        numb_fromdb = BotDB.get_datanumb(user_id=message.from_user.id)
        numb_fromdb = int(numb_fromdb[0])
        numcount_fromdb = BotDB.get_numbercount(user_id=message.from_user.id)
        c1 = int(numcount_fromdb[0])
        restate = BotDB.get_restate(user_id=message.from_user.id)
        restate = bool(restate[0])
        a1 = func.min_num(numa_fromdb, numb_fromdb)
        b1 = func.max_num(numa_fromdb, numb_fromdb)
        if restate == False:
            result = str(func.numgenerate(a1, b1, c1))
            await message.answer(f'Остання дія - вибір з діапазону чисел від {numa_fromdb} '
                                 f'до {numb_fromdb}, {c1} разів.'
                                 f'\nРандомнi числa з діапазону: {result}')
        elif (restate == True) and (c1 <= (b1 - a1 + 1)):
            result = str(func.numgenerateon(a1, b1, c1))
            await message.answer(f'Остання дія - вибір з діапазону чисел від {numa_fromdb} '
                                 f'до {numb_fromdb}, {c1} разів,'
                                 f' без повторів.\nРандомнi числa з діапазону: {result}')
        else:
            await message.answer('Умова неможлива! Кількість згенерованих чисел не може бути '
                                 'більша за кількість можливих неповторюваних чисел! Вимкніть '
                                 'функцію "Без повторів" або вкажіть меншу кількість чисел'
                                 ' для генерації.')
    elif actionstate == 2:
        a = BotDB.get_list(message.from_user.id)
        a = a[0]
        listholder = func.list_to_mass(a)
        i = random.randint(0, len(listholder) - 1)
        await message.answer(f"Остання дія - вибір обєкта із заданого списку"
                             f"\nВипадковий об'єкт зі списку: {listholder[i]}")

