import time
import random

valute = "руб."
money = 1000
startMoney = 0
play = True

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
            d2 -= 1
        if (getD3):
            d3 += 1
        if (getD4):
            d4 -= 1
        if (getD5):
            d5 += 1

        if(d1>9):
            d1 = 0
        if (d2 < 0):
            d2 = 9
        if (d3 > 9):
            d3 = 0
        if (d4 < 0):
            d4 = 9
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
        print(f"    {d1} {d2} {d3} {d4} {d5}")

    maxCount = getMaxCount(d1,d1,d2,d3,d4,d5)

    if(maxCount < getMaxCount(d2,d1,d2,d3,d4,d5)):
        maxCount = getMaxCount(d2,d1,d2,d3,d4,d5)
    if (maxCount < getMaxCount(d3, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d3, d1, d2, d3, d4, d5)
    if (maxCount < getMaxCount(d4, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d4, d1, d2, d3, d4, d5)
    if (maxCount < getMaxCount(d5, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d5, d1, d2, d3, d4, d5)

    if(maxCount == 2):
        print(f"Совпадение двух чисел.")
    elif(maxCount == 3):
        res *= 2
        print(f"Совпадение трех чисел. Твой выйгрыш {res/2}")
    elif (maxCount == 4):
        res *= 5
        print(f"Совпадение четырех чисел. Твой выйгрыш {res}")
    elif (maxCount == 5):
        res *= 10
        print(f"Совпадение всех чисел. Твой выйгрыш {res}")

    else:
        lose(res)
        res = 0
    input("Нажми enter")
    return res


def oneHand():
    global money
    playGame = True
    while(playGame):
        print("Однорукий бандит")
        print(f"у тебя на счету {money} {valute}")
        rate = int(input("ставка")) #ставка
        money -= rate
        money += getRes(rate)

        if(money <= 0):
            playGame = False


def getRoulette(visible):
    tickTime = random.randint(100,200) / 10000
    mainTime = 0
    number = random.randint(0,38)
    Ttime = random.randint(100,110) / 100
    col = 1

    while(mainTime < 0.3):
        col += 1
        if(col > 15):
            col = 1
        mainTime += tickTime
        tickTime *= Ttime

        number += 1
        if(number > 39):
            number = 0
            print()

        printNumber = number

        print(" Число ", printNumber, "*" * number," "*(79 - number * 2), "*" * number)
        if (visible):
            time.sleep(mainTime)
    return number

def roulete():
    global  money
    playGame = True
    while(playGame and money > 0):
        print(f"у тебя на счету {money} {valute}")
        print("ставка на ")
        print("1. Четное")
        print("2. Не четное")
        print("3. Дюжина")
        print("4. Число")
        x = int(input())
        playRoulette = True
        if(x == 3):
            print("Выбери числа")
            print("1. 1-12")
            print("2. 13-24")
            print("3. 25-36")
            print("0. exit")
            dz = int(input())
            if(dz == 1):
                tD = "1-12"
            elif (dz == 2):
                tD = "13-24"
            elif (dz == 3):
                tD = "25-36"
            elif(dz == 0):
                playRoulette = False
        elif(x == 4):
                number = int(input("какое?"))
        elif(x == 0):
                return 0
        if(playRoulette):
            print("Ставка?")
            stavka = int(input())
            rez = getRoulette(True)

            if(rez < 37):
                print(f"выпало число {rez} ")

                if(x == 1):
                    print("ставка на четное")
                    if (rez < 37 and rez % 2 == 0):
                        money += stavka
                        win(stavka)
                    else:
                        money -= stavka
                        lose(stavka)

                elif(x == 2):
                    print("ставка на не четное")
                    if (rez < 37 and rez % 2 != 0):
                        money += stavka
                        win(stavka)
                    else:
                        money -= stavka
                        lose(stavka)

                elif(x == 3):
                    print(f"ставка на диапазон чисел {tD}")
                    winD = ""
                    if(rez > 0 and rez < 13):
                        winD = 1
                    elif (rez > 12 and rez < 25):
                        winD = 2
                    elif (rez > 24 and rez < 37):
                        winD = 3
                    if(dz == winD):
                        money += stavka * 2
                        win(stavka*2)
                    else:
                        money -= stavka
                        lose(stavka)
                        print()
                        input("Нажмите enter")
                elif( x == 4):
                    print(f"ставка сделана на число {number}")
                    if(rez == number):
                        money += stavka * 35
                        win(stavka*35)
                    else:
                        money -= stavka
                        lose(stavka)


def main():
    global money,play

    startMoney = money

    while(play and money > 0):
        print(f"у тебя на счету {money} {valute}")
        print("Ты можешь сыграть в")
        print(" 1. Рулетку")
        print(" 2. Слоты")
        print(" 0. Выход")

        x = int(input())
        if(x == 0):
            play = False
        elif(x == 1):
            roulete()
        elif (x == 2):
            oneHand()
    if ( money <= 0):
        print("money over")

    if(money > startMoney):
        print("congratulations")
    else:
        print("you lose")

main()# вызов

