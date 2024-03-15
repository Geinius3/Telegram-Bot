from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Куби'),KeyboardButton(text='Обрати число')],
    [KeyboardButton(text='Вибрати зі списку')],
    [KeyboardButton(text='Повторити дію')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Оберіть пункт меню.')

cubes = ['D4','D6','D8','D10','D12','D20']

async def inline_cubes():
    keyboard = InlineKeyboardBuilder()
    for cube in cubes:
        keyboard.add(InlineKeyboardButton(text=cube, callback_data=f'cube_{cube}'))
    return keyboard.adjust(3).as_markup()

startmesskb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Тицни',url='https://youtu.be/j-iheFkstFQ')]
])

choosenumkb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Показати число',  callback_data=f'shownum')],
    [InlineKeyboardButton(text='Задати кількість чисел',  callback_data=f'countnums')],
    [InlineKeyboardButton(text='Без повторів', callback_data=f'repeatson')]
])



#Клавітура команди хелп
helplist = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Start', callback_data=f'startinfo')],
    [InlineKeyboardButton(text='Help', callback_data=f'helpinfo')],
    [InlineKeyboardButton(text='Random Sticker', callback_data=f'randstickinfo')]
])