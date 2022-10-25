# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
list = [1, 2, 3]
print("Выберите режим игры: \n 1 - человек и человек \n 2 - человек и бот \n 3 - человек и супербот")
mode = int(input("Введите режим: "))
while mode not in list:
    print("Неверный код. Введтие заново.")
    mode = int(input("Введите режим: "))

if mode == 1:
    players = [1, 2]
    players_sum = [0, 0]
    print("Режим человек - человек.")
    players[0] = str(input("Введите имя первого игрока: "))
    players[1] = str(input("Введите имя второго игрока: "))
    start = int(input("Введите количество конфет: "))
    confets = start
    print("Начинаем игру!")
    print("Количество конфет:", confets)

    player = random.randint(0, 1)
    while confets > 0:
        player = not player
        if player == True:
            pl = 0
        else:
            pl = 1
        print("Ход пользователя ", players[pl])
        hod = int(input("Введите количество конфет: "))
        if hod > 28 or hod < 1:
            print("Можно взять от 1 до 28 конфет за один ход!")
            player = not player
        else:
            if confets < hod:
                hod = confets
            confets = confets - hod
            players_sum[pl] += hod

            print("Спасибо! Конфет осталось: ", confets)

    print("Игра окончена!")
    print("Выиграл игрок ", players[pl])
    print("Приз: ", players_sum[pl], "своих", " + ", start - players_sum[pl], "конфет оппонента!")

elif mode == 2:
    players = [1, 2]
    players_sum = [0, 0]
    print("Режим человек - бот.")
    players[0] = str(input("Введите имя игрока: "))
    players[1] = "Bot-Konfetoed"
    start = int(input("Введите количество конфет: "))
    confets = start
    print("Начинаем игру!")
    print("Количество конфет:", confets)

    player = random.randint(0, 1)
    while confets > 0:
        player = not player
        if player == True:
            pl = 0
        else:
            pl = 1
        print("Ход пользователя ", players[pl])
        if pl == 0:
            hod = int(input("Введите количество конфет: "))
            if hod > 28 or hod < 1:
                print("Можно взять от 1 до 28 конфет за один ход!")
                player = not player
            else:
                if confets < hod:
                    hod = confets
                confets = confets - hod
                players_sum[pl] += hod
        else:
            hod = random.randint(1, 28)
            print(players[1], "взял ", hod, "конфет")
            if confets < hod:
                hod = confets
            confets = confets - hod
            players_sum[pl] += hod
        print("Спасибо! Конфет осталось: ", confets)

    print("Игра окончена!")
    print("Выиграл игрок ", players[pl])
    print("Приз: ", players_sum[pl], "своих", " + ", start - players_sum[pl], "конфет оппонента!")

else:

    players = [1, 2]
    players_sum = [0, 0]
    print("Режим человек - супербот.")
    players[0] = str(input("Введите имя игрока: "))
    players[1] = "Super-Bot-Konfetoed"
    start = int(input("Введите количество конфет: "))
    confets = start
    print("Начинаем игру!")
    print("Количество конфет:", confets)

    player = random.randint(0, 1)
    while confets > 0:
        player = not player
        if player == True:
            pl = 0
        else:
            pl = 1
        print("Ход пользователя ", players[pl])
        if pl == 0:
            hod = int(input("Введите количество конфет: "))
            if hod > 28 or hod < 1:
                print("Можно взять от 1 до 28 конфет за один ход!")
                player = not player
            else:
                if confets < hod:
                    hod = confets
                confets = confets - hod
                players_sum[pl] += hod
        else:
            hod = confets % 29
            if hod == 0:
                hod = random.randint(1, 28)
            print(players[1], "взял ", hod, "конфет")

            if confets < hod:
                hod = confets
            confets = confets - hod
            players_sum[pl] += hod
        print("Спасибо! Конфет осталось: ", confets)

    print("Игра окончена!")
    print("Выиграл игрок ", players[pl])
    print("Приз: ", players_sum[pl], "своих", " + ", start - players_sum[pl], "конфет оппонента!")
