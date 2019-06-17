import os
from action import Action
from board import Item


commands = {
    Action.EXIT: "0",
    Action.DOWN: "2",
    Action.LEFT: "4",
    Action.RIGHT: "6",
    Action.UP: "8"
}


def get_action(inputKey):
    for action, key in commands.items():
        if key == inputKey:
            return action
    return Action.UNKNOWN


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_game(board):
    border = get_top_border(board)
    print(border)
    for row in board:
        line = "\u25ae "
        for cell in row:
            if cell == Item.PAWN:
                line += "\u25b2 "
            elif cell == Item.FENCE:
                line += "\u25fc "
            elif cell == Item.SQUARE:
                line += "\u25a1 "
            else:
                line += "  "
        line += "\u25ae"
        print(line)
    print(border)


def get_top_border(board):
    border = "\u25ac"
    for x in board:
        border += "\u25ac\u25ac"
    border += "\u25ac\u25ac"
    return border


def prompt_action():
    key = prompt("Where do you want to move the pawn?\nChoose in list and type ENTER " + get_action_list())
    return get_action(key)


def get_action_list():
    message = "("
    for action, key in commands.items():
        message += action.name + ": " + key + ", "
    message = message[:-2]
    message += ")"
    return message


def prompt(message):
    return input(message)


def display(message):
    print(message)
