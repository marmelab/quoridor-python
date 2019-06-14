import math
from pawn import Pawn, translate_x, translate_y
from exception import OutOfBoardException
from functools import reduce
from action import Action
import console

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


def progress(pawn):
    new_pawn = pawn
    quit = False
    victory = False
    console.clear()
    console.prompt("** Welcome to PyQuoridor **\n  Press Enter to start ...")
    while not(quit or victory):
        display(new_pawn)
        action = console.prompt_action()
        if action == Action.EXIT:
            quit = True
        else:
            try:
                new_pawn = act(action, new_pawn)
            except OutOfBoardException:
                pass
        victory = is_a_victory(new_pawn)
    if victory:
        display(new_pawn)
        console.display("** You won **")


def display(pawn):
    console.clear()
    board = get_board(pawn)
    console.display_game(board)


def is_a_victory(pawn):
    return pawn.x == BASE_LINE_SIZE - 1


def act(action, pawn):
    new_pawn = pawn
    if action == Action.RIGHT:
        new_pawn = translate_x(pawn, 1)
    elif action == Action.LEFT:
        new_pawn = translate_x(pawn, -1)
    elif action == Action.DOWN:
        new_pawn = translate_y(pawn, 1)
    elif action == Action.UP:
        new_pawn = translate_y(pawn, -1)
    if (is_out_of_board(new_pawn)):
        raise OutOfBoardException("The pawn is out of the board")
    return new_pawn
