import math
from pawn import Pawn

BASE_LINE_SIZE = 9


def init_game():
    center = math.floor(BASE_LINE_SIZE / 2)
    return Pawn(0, center)


def get_board(pawn):
    board = []
    for y in range(BASE_LINE_SIZE):
        line = []
        for x in range(BASE_LINE_SIZE):
            if (pawn.x == x and pawn.y == y):
                line.append(1)
            else:
                line.append(0)
        board.append(line)
    return board


def display_board(board):
    border = get_top_border(board)
    print(border)
    for x in board:
        line = "# "
        for y in x:
            if (y == 1):
                line += "P "
            else:
                line += ". "
        line += "#"
        print(line)
    print(border)


def get_top_border(board):
    border = "#"
    for x in board:
        border += "##"
    border += "##"
    return border
