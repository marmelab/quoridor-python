import math
from random import randint
from copy import deepcopy
from enum import IntEnum
from exception import OutOfBoardException, QuoridorException

FENCE_SIZE = 8
BASE_LINE_SIZE = 17
FENCE_NUMBER = 10


class Item(IntEnum):
    NO_FENCE = 0
    FENCE = 1
    SQUARE = 2
    PAWN_1 = 3
    PAWN_2 = 4


class Direction(IntEnum):
    NO = 0
    HORIZONTALLY = 1
    VERTICALLY = 2


class Fence:

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction


def build():
    fences = [[Direction.NO for i in range(FENCE_SIZE)] for j in range(FENCE_SIZE)]
    for i in range(FENCE_NUMBER):
        fence = add_random_fence(fences)
        fences[fence.y][fence.x] = fence.direction
    return fences


def add_random_fence(fences):
    center_x = randint(0, FENCE_SIZE - 1)
    center_y = randint(0, FENCE_SIZE - 1)
    direction = randint(Direction.HORIZONTALLY, Direction.VERTICALLY)
    if can_add_fence(fences, center_x, center_y, direction):
        return Fence(center_x, center_y, direction)
    return add_random_fence(fences)


def can_add_fence(fences, x, y, direction):
    if not is_fence_inside_grid(x, y, fences) or direction == Direction.NO:
        return False
    fence = fences[y][x]
    if fence != Direction.NO:
        return False
    if direction == Direction.HORIZONTALLY:
        previous_fence = get_fence_direction(fences, x - 1, y)
        next_fence = get_fence_direction(fences, x + 1, y)
        return previous_fence != Direction.HORIZONTALLY and next_fence != Direction.HORIZONTALLY
    if direction == Direction.VERTICALLY:
        previous_fence = get_fence_direction(fences, x, y - 1)
        next_fence = get_fence_direction(fences, x, y + 1)
        return previous_fence != Direction.VERTICALLY and next_fence != Direction.VERTICALLY
    return True


def get_fence_direction(fences, x, y):
    return Direction.NO if not is_fence_inside_grid(x, y, fences) else fences[y][x]


def is_fence_inside_grid(x, y, fences):
    return is_inside_fences(x, fences) and is_inside_fences(y, fences)


def is_inside_fences(coord, fences):
    return coord >= 0 and coord < len(fences)


def get_board(pawns, fences):
    board = get_empty_board()
    i = 0
    for pawn in pawns:
        if (is_out_of_board(pawn)):
            raise OutOfBoardException("The pawn is out of the board")
        board[pawn.y][pawn.x] = get_pawn_item(i)
        i += 1
    return add_fences(board, fences)


def get_pawn_item(index):
    return Item.PAWN_1 if index == 0 else Item.PAWN_2


def get_empty_board():
    return [[Item.NO_FENCE if is_odd(x) or is_odd(y) else Item.SQUARE for x in range(BASE_LINE_SIZE)] for y in range(BASE_LINE_SIZE)]


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


def is_crossable_right(pawn, fences):
    if pawn.x == BASE_LINE_SIZE - 1:
        return False
    top_right_fence = get_top_right_fence(pawn, fences)
    bottom_right_fence = get_bottom_right_fence(pawn, fences)
    return is_crossable_horizontally(top_right_fence, bottom_right_fence)


def is_crossable_left(pawn, fences):
    if pawn.x == 0:
        return False
    top_left_fence = get_top_left_fence(pawn, fences)
    bottom_left_fence = get_bottom_left_fence(pawn, fences)
    return is_crossable_horizontally(top_left_fence, bottom_left_fence)


def is_crossable_up(pawn, fences):
    if pawn.y == 0:
        return False
    top_left_fence = get_top_left_fence(pawn, fences)
    top_right_fence = get_top_right_fence(pawn, fences)
    return is_crossable_vertically(top_left_fence, top_right_fence)


def is_crossable_down(pawn, fences):
    if pawn.y == BASE_LINE_SIZE - 1:
        return False
    bottom_left_fence = get_bottom_left_fence(pawn, fences)
    bottom_right_fence = get_bottom_right_fence(pawn, fences)
    return is_crossable_vertically(bottom_left_fence, bottom_right_fence)


def is_crossable_horizontally(first_fence, second_fence):
    return first_fence != Direction.VERTICALLY and second_fence != Direction.VERTICALLY


def is_crossable_vertically(first_fence, second_fence):
    return first_fence != Direction.HORIZONTALLY and second_fence != Direction.HORIZONTALLY


def get_top_left_fence(pawn, fences):
    return get_fence(pawn.x - 1, pawn.y - 1, fences)


def get_top_right_fence(pawn, fences):
    return get_fence(pawn.x + 1, pawn.y - 1, fences)


def get_bottom_left_fence(pawn, fences):
    return get_fence(pawn.x - 1, pawn.y + 1, fences)


def get_bottom_right_fence(pawn, fences):
    return get_fence(pawn.x + 1, pawn.y + 1, fences)


def get_fence(x, y, fences):
    fence_x = math.ceil(x / 2) - 1
    fence_y = math.ceil(y / 2) - 1
    direction = None
    if inside(fence_x) and inside(fence_y):
        direction = fences[fence_y][fence_x]
    else:
        direction = Direction.NO
    return direction


def inside(coord):
    return coord >= 0 and coord < FENCE_SIZE
