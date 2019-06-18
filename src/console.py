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


def get_action(input_key):
    for action, key in commands.items():
        if key == input_key:
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
            if cell == Item.PAWN_1:
                line += "\033[94m\u25b2\033[0m "
            elif cell == Item.PAWN_2:
                line += "\033[92m\u25b2\033[0m "
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


def prompt_action(player_number):
    print("Possible actions: " + get_action_list())
    key = prompt(f"Player # {player_number}: Where do you want to move the pawn? ")
    return get_action(key)


def get_action_list():
    message = "("
    message += ", ".join([f"{action.name}: {key}" for action, key in commands.items()])
    message += ")"
    return message


def prompt(message):
    return input(message)


def display(message):
    print(message)
