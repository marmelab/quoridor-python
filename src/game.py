import math
from pawn import Pawn
from exception import OutOfBoardException
from functools import reduce

BASE_LINE_SIZE = 9


def init_game():
    center = math.floor(BASE_LINE_SIZE / 2)
    return Pawn(0, center)


def get_board(pawn):
    if (is_out_of_board(pawn)):
        raise OutOfBoardException("The pawn is out of the board")
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


def is_out_of_board(pawn):
    return is_out_of_base_line(pawn.x) or is_out_of_base_line(pawn.y)


def is_out_of_base_line(coord):
    return coord < 0 or coord >= BASE_LINE_SIZE


def display_board(board):
    border = get_top_border(board)
    print(border)
    
    for row in board:
        line = "# "
        line += "".join(["P " if (y ==1) else ". " for y in row])
        line += "#"
        print(line)
    print(border)


def get_top_border(board):
    border = "#"
    for x in board:
        border += "##"
    border += "##"
    return border
