import time
import random
from _ctypes import *

valute = "руб."
money = 0
startMoney = 0
play = True
default = 10000

def win(result):
    print(f"Победа! {result}{valute}")
    print(f"Баланс : {money}")

def lose(result):
    print(f"Проигрыш!{result}{valute}")
    print({f"Баланс : {money}"})

def getMaxCount(digit,v1,v2,v3,v4,v5):
    ret = 0
    if(digit == v1):
        ret +=1
    if (digit == v2):
        ret += 1
    if (digit == v3):
        ret += 1
    if (digit == v4):
        ret += 1
    if (digit == v5):
        ret += 1
    return ret

def getRes(rate):
    res = rate
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0

    getD1 = True
    getD2 = True
    getD3 = True
    getD4 = True
    getD5 = True
    col = 10

    while(getD1 or getD2 or getD3 or getD4 or getD5):
        if(getD1):
            d1 += 1
        if (getD2):
            d2 += 1
        if (getD3):
            d3 += 1
        if (getD4):
            d4 += 1
        if (getD5):
            d5 += 1

        if(d1>9):
            d1 = 0
        if (d2 > 9):
            d2 = 0
        if (d3 > 9):
            d3 = 0
        if (d4 > 9):
            d4 = 0
        if (d5 > 9):
            d5 = 0

        if(random.randint(0,20) == 1):
            getD1 = False
        if (random.randint(0, 20) == 1):
            getD2 = False
        if (random.randint(0, 20) == 1):
            getD3 = False
        if (random.randint(0, 20) == 1):
            getD4 = False
        if (random.randint(0, 20) == 1):
            getD5 = False

        time.sleep(0.1)
        col +=1
        if(col > 15):
            col = 10
        print("   " + "%" * 10)
        print(f"{d1} {d2} {d3} {d4} {d5}")

    maxCount = getMaxCount(d1,d1,d2,d3,d4,d5)
    if(maxCount == 2):
        print(f"овпадение двух чисел. Твой выйгрыш {res}")
    elif(maxCount == 3):
        res *= 2
        print(f"Совпадение трех чисел. Твой выйгрыш {res}")
    elif (maxCount == 4):
        res *= 5
        print(f"Совпадение четырех чисел. Твой выйгрыш {res}")
    elif (maxCount == 5):
        res *= 10
        print(f"Совпадение всех чисел. Твой выйгрыш {res}")

    else:
        lose(res)
        input("Нажми enter")
        return res


def oneHand():
    global money
    playGame = True
    while(playGame):
        print("Однорукий бандит")
        print(f"у тебя на счету {money} {valute}")
        rate = input("ставка") #ставка
        money -= rate
        money += getRes(rate)

        if(money <= 0):
            playGame = False