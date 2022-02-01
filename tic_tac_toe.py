from random import randint

board = [
    ["", "0", "1", "2"],
    ["0", "-", "-", "-"],
    ["1", "-", "-", "-"],
    ["2", "-", "-", "-"]
]


# Вывод доски в консоль
def print_board(board):
    for i in board:
        for j in i:
            print(j, end='\t')
        print()


# Проверка на победу
def check_board(board, token):

    if ((board[1][1] == token and board[1][2] == token and board[1][3] == token) or
       (board[2][1] == token and board[2][2] == token and board[2][3] == token) or
       (board[3][1] == token and board[3][2] == token and board[3][3] == token) or
       (board[1][1] == token and board[2][1] == token and board[3][1] == token) or
       (board[1][2] == token and board[2][2] == token and board[3][2] == token) or
       (board[1][3] == token and board[2][3] == token and board[3][3] == token) or
       (board[1][1] == token and board[2][2] == token and board[3][3] == token) or
       (board[3][1] == token and board[2][2] == token and board[1][3] == token)):
        result = True
    else:
        result = False
    return result


# Определение первого хода
def first_in():
    first = randint(0, 1)
    if first == 0:
        result = ["Компьютер", "Х"]
    else:
        result = ["Игрок", "Х"]
    return result


# Ход Компьютера
def comp_step(board):
    x = randint(1, 3)
    y = randint(1, 3)
    return (x, y) if board[x][y] == "-" else comp_step(board)

# Основной цикл игры
def main(board):
    game_board = board.copy()
    next_step = first_in()
    counter = 0
    game = True
    print(f'Первым ходит {next_step[0]}, играя "{next_step[1]}"')
    if next_step[0] == "Игрок":
        print_board(game_board)

    while game:
        if next_step[0] == "Компьютер":
            print("Ход Компьютера")
            step = comp_step(game_board)
            game_board[step[0]][step[1]] = next_step[1]
            print_board(game_board)
            counter += 1
            if counter > 4:
                if check_board(game_board, next_step[1]):
                    print(f"Игра окончена. Победил {next_step[0]}!")
                    game = False
                if counter == 9:
                    print("Ничья!")
                    game = False
            next_step[0], next_step[1] = "Игрок", "О" if next_step[1] != "О" else "Х"
        else:
            step = None
            while True:
                try:
                    step = tuple(map(int, input("Ход Игрока. Введите координаты для хода через запятую : ").split(',')))
                    if not(step[0] in range(0, 3)) or not(step[1] in range(0, 3)):
                        print("Вводите координаты в интервале от 0 до 2")
                        continue
                    elif game_board[step[0] + 1][step[1] + 1] in "ХО":
                        print("Клетка уже занята!!!")
                        continue
                    else:
                        break
                except ValueError:
                    print("Введены не числовые значения, вводите числа через запятую")
                    continue
            game_board[step[0] + 1][step[1] + 1] = next_step[1]
            print_board(game_board)
            counter += 1
            if counter > 4:
                if check_board(game_board, next_step[1]):
                    print(f"Игра окончена. Победил {next_step[0]}!")
                    game = False
                if counter == 9:
                    print("Ничья!")
                    game = False
            next_step[0], next_step[1] = "Компьютер", "О" if next_step[1] != "О" else "Х"


main(board)
