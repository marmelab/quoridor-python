import os
from action import UP, DOWN, LEFT, RIGHT, EXIT


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_game(board):
    border = get_top_border(board)
    print(border)
    for row in board:
        line = "# "
        line += "".join(["P " if y == 1 else ". " for y in row])
        line += "#"
        print(line)
    print(border)


def get_top_border(board):
    border = "#"
    for x in board:
        border += "##"
    border += "##"
    return border


def prompt_action():
    invalid = True
    move = 0
    while invalid:
        message = "Where do you want to move the pawn?\n" + \
            "Choose in list and type ENTER (UP: {}, RIGHT: {}, DOWN: {}, LEFT: {} EXIT: {})\n" \
            .format(UP, RIGHT, DOWN, LEFT, EXIT)
        action = prompt(message)
        try:
            move = int(action)
            invalid = False
        except ValueError:
            invalid = True
    return move


def prompt(message):
    return input(message)


def display(message):
    print(message)
