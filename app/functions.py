import random
import config



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

#Рандомний стікер
sticklist = config.STICKER_LIST
def rand_stick(sticklist):
    i = random.randint(0, len(sticklist)-1)
    return sticklist[i]

listin = config.LIST_TASKS
def list_choose(listin):
    listout = listin.split(',')
    i = random.randint(0, len(listout)-1)
    return listout[i]


#Функція перетворення строки на масив
def list_to_mass(objlist):
    listout = objlist.split(',')
    return listout

#ФУнкція генерації чисел
def numgenerate(numa,numb,numc):
    i = 0
    numlist = []
    while i < numc:
        numlist.append(random.randint(numa, numb))
        i += 1
    else:
        result = str(numlist[0:numc])
        newres = ''
        for i in range(len(result)):
            if i != 0 and i != len(result) - 1:
                newres += result[i]
        return newres

def numgenerateon (numa,numb,numc):
    numlist = []
    while len(numlist) < numc:
        i = random.randint(numa,numb)
        if i not in numlist:
            numlist.append(i)
    else:
        result = str(numlist[0:numc])
        newres = ''
        for i in range(len(result)):
            if i != 0 and i != len(result) - 1:
                newres += result[i]
        return newres

def which_state (restate):
    On = 'ON'
    Off = 'OFF'
    if restate == True:
        return On
    elif restate == False:
        return Off
