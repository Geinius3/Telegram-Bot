from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Куби'),KeyboardButton(text='Обрати число')],
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



