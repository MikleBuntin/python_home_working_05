# Создайте программу для игры в ""Крестики-нолики"".

# print("  ____________\nC|___|___|___|\nB|___|___|___|\nA|___|___|___|\n*| 1 | 2 | 3 |")

import random
def print_pole(pole):
    print("   ", end='')
    for n in range(len(pole[0])):
        print("", n + 1, "|", end='')
    print()

    for i in range(len(pole)):
        print(i + 1, "| ", end='')
        for j in range(len(pole[i])):
            if pole[i][j] == 0:
                print(" ", "|", end=' ')
            else:
                print(pole[i][j], "|", end=' ')
        print()
    # print("  |", end='')

strings = int(input("Введите количество строк: "))
tables = int(input("Введите количество столбцов: "))

pole = [[0] * tables for i in range(strings)]
print_pole(pole)


players = [[1, "X"], [2, "O"]]
players[0][0] = str(input("Введите имя первого игрока (O): "))
players[1][0] = str(input("Введите имя второго игрока (X): "))
print("Начинаем игру!")
pobeda = 0
player = random.randint(0, 1)
while pobeda == 0:
    player = not player
    if player == True:
        pl = 0
    else:
        pl = 1
    print("Ход пользователя ", players[pl][0])
    # print_pole(pole)
    hod = str(input("Введите координаты хода (строка, столбец): "))
    if hod == "!":
        break
    hod = hod.split(', ')
    hod = [int(hod[0]), int(hod[1])]
    # print(hod)
    # print(players[player][1])
    if pole[hod[0] - 1][hod[1] - 1] == 0:
        pole[hod[0] - 1][hod[1] - 1] = players[player][1]
    else:
        print("Эта клетка занята!")
        player = not player
    print_pole(pole)

print("Игра окончена!")