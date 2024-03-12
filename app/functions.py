import random
listin = 'пресс качат,анжуманя,бегит,турник'
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