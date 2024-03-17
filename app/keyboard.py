from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

#Основна клавіатура
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Куби'),KeyboardButton(text='Обрати число')],
    [KeyboardButton(text='Додати куб'),KeyboardButton(text='Вибрати зі списку')],
    [KeyboardButton(text='Повторити дію')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Оберіть пункт меню.')


#Клавіатура кубів
"""cubes = ['D4','D6','D8','D10','D12','D20']"""

async def inline_cubes(list):
    keyboard = InlineKeyboardBuilder()
    i = 0
    for cube in list:
        if list[i] != '0' and i < 6:
            keyboard.add(InlineKeyboardButton(text=f'D{cube}', callback_data=f'cube_D{cube}'))
        elif 6 <= i <= 8 and list[i] != '0':
            keyboard.add(InlineKeyboardButton(text=f'D{list[i]}', callback_data=f'cube_N{i}'))
        i+=1
    return keyboard.adjust(3).as_markup()

#рікрол
startmesskb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Тицни',url='https://youtu.be/j-iheFkstFQ')]
])

#клавіатура до вибору числа
choosenumkb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Згенерувати числа',  callback_data=f'shownum')],
    [InlineKeyboardButton(text='Задати кількість чисел',  callback_data=f'countnums')],
    [InlineKeyboardButton(text='Без повторів', callback_data=f'repeatson')]
])



#Клавітура команди хелп
helplist = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Start', callback_data=f'startinfo'),
     InlineKeyboardButton(text='Help', callback_data=f'helpinfo')],
    [InlineKeyboardButton(text='Random Sticker', callback_data=f'randstickinfo'),
     InlineKeyboardButton(text='Куби', callback_data=f'cubeinfo')],
    [InlineKeyboardButton(text='Додати куб', callback_data=f'addcubeinfo'),
     InlineKeyboardButton(text='Обрати число', callback_data=f'choosenuminfo')],
    [InlineKeyboardButton(text='Вибрати зі списку', callback_data=f'chooselistinfo'),
     InlineKeyboardButton(text='Повторити дію', callback_data=f'repeatinfo')]
])