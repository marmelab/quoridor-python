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


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_game(board):
    border = get_top_border(board)
    print(border)
    for row in board:
        line = "# "
        for cell in row:
            if cell == Item.PAWN:
                line += "▲ "
            elif cell == Item.FENCE:
                line += "# "
            elif cell == Item.SQUARE:
                line += "□ "
            else:
                line += "  "
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
            .format(commands[Action.UP], commands[Action.RIGHT], commands[Action.DOWN], commands[Action.LEFT], commands[Action.EXIT])
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
