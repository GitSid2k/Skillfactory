import colorama
from colorama import Fore, Back, Style
colorama.init()


def greet():
    print(Fore.LIGHTGREEN_EX + "", "_" * 17)
    print("  Приветствуем Вас  ")
    print("       в игре       ")
    print("   крестики-нолики  ")
    print("", "_" * 17)
    print(" формат ввода: x y  ")
    print(" x - номер строки   ")
    print(" y - номер столбца  " + Fore.RESET)


greet()
field = [[" "] * 3 for i in range(3)]


def show():
    print()
    print("   | 0 | 1 | 2 |")
    print("", "_" * 15)
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print("", "_" * 15)
    print()


def ask():
    while True:

        cords = input("       Ваш ход:").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def check_win():
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coord in win_coord:
        symbols = []
        for c in coord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["x", "x", "x"]:
            show()
            print(Fore.LIGHTBLUE_EX + 'Выиграл "x"!!!')
            return True
        if symbols == ["o", "o", "o"]:
            show()
            print(Fore.LIGHTYELLOW_EX + 'Выиграл "o"!!!')
            return True
    return False


count = 0

while True:
    count += 1
    show()

    if count % 2 == 1:
        print(" Ходит крестик ")
    else:
        print(" Ходит нолик")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "x"
    else:
        field[x][y] = "o"

    if check_win():
        break

    if count == 9:
        print(Fore.RED + "Ничья")
        break
