"""
Использую функцию из предыдущей задачи, написать программу игру Блэкджек,
т.е. реализовать цикл в котором на каждом ходу у игрока спрашивается, достать ли следующую карту,
в случае положительного ответа  - вытягивать случайную карту. Игра заканчивается если игрок отказывается брать карту,
либо сумма его карт больше 21-го.
"""


import random


number_card = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "D", "K", "A"]
counter = 0
number = 0


while True:

    move = input("Взять карту?(да/нет) ")
    if "да" in move:
        card = (f"{random.choice(number_card)}")
    if "2345678910" in card:
        number = int(card)
    if "JDK" in card:
        number = 10
    if "A" in card:
        if counter < 21:
            number = 11
        else:
            number = 1
    counter += number
    if counter < 21:
        print('конец игры')
        break
    if "нет" in move:
        print("конец игры")
        break






