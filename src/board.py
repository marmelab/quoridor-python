import math
from random import randint
from copy import deepcopy 
from enum import IntEnum
from exception import OutOfBoardException

FENCE_SIZE = 8
BASE_LINE_SIZE = 17


class Item(IntEnum):
    NO_FENCE = 0
    FENCE = 1
    SQUARE = 2
    PAWN = 3


class Direction(IntEnum):
    NO = 0
    HORIZONTALLY = 1
    VERTICALLY = 2


def build():
    fences = [[Direction.NO for i in range(FENCE_SIZE)] for j in range(FENCE_SIZE)]
    for i in range(10):
        center_x = randint(0, FENCE_SIZE - 1)
        center_y = randint(0, FENCE_SIZE - 1)
        direction = randint(Direction.HORIZONTALLY, Direction.VERTICALLY)
        fences[center_x][center_y] = direction
    return fences


def get_board(pawn, fences):
    if (is_out_of_board(pawn)):
        raise OutOfBoardException("The pawn is out of the board")
    board = generate_default_board(pawn)
    return add_fences(board, fences)


def generate_default_board(pawn):
    board = []
    for y in range(BASE_LINE_SIZE):
        line = []
        for x in range(BASE_LINE_SIZE):
            if pawn.x == x and pawn.y == y:
                line.append(Item.PAWN)
            elif is_odd(x) or is_odd(y):
                line.append(Item.NO_FENCE)
            else:
                line.append(Item.SQUARE)
        board.append(line)
    return board


def is_odd(number):
    return number % 2 != 0


def add_fences(board, fences):
    new_board = deepcopy(board)
    for x in range(FENCE_SIZE):
        for y in range(FENCE_SIZE):
            center_x = x * 2 + 1
            center_y = y * 2 + 1
            direction = fences[x][y]
            if direction == Direction.HORIZONTALLY:
                new_board[center_x][center_y - 1] = Item.FENCE
                new_board[center_x][center_y] = Item.FENCE
                new_board[center_x][center_y + 1] = Item.FENCE
            elif direction == Direction.VERTICALLY:
                new_board[center_x - 1][center_y] = Item.FENCE
                new_board[center_x][center_y] = Item.FENCE
                new_board[center_x + 1][center_y] = Item.FENCE
    return new_board


def is_out_of_board(pawn):
    return is_out_of_base_line(pawn.x) or is_out_of_base_line(pawn.y)


def is_out_of_base_line(coord):
    return coord < 0 or coord >= BASE_LINE_SIZE
