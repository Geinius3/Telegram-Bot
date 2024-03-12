import random

import config
listin = config.LIST_TASKS
def list_choose(listin):
    listout = listin.split(',')
    i = random.randint(0, len(listout)-1)
    return listout[i]

#Максимальне число з двох
def max_num(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return b

#Мінімальне число з двох
def min_num(a, b):
    if a < b:
        return a
    elif b < a:
        return b
    else:
        return a

sticklist = config.STICKER_LIST
def rand_stick(sticklist):
    i = random.randint(0, len(sticklist)-1)
    return sticklist[i]

#Функція перетворення строки на масив
def list_to_mass(objlist):
    listout = objlist.split(',')
    return listout