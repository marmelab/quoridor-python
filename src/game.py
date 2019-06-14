import math
from pawn import Pawn, translate_x, translate_y
from exception import OutOfBoardException
from functools import reduce
from action import Action
import console
from board import *


def init_game():
    center = math.floor(BASE_LINE_SIZE / 2)
    return Pawn(0, center)


def progress(pawn):
    new_pawn = pawn
    new_fences = build()
    quit = False
    victory = False
    console.clear()
    console.prompt("** Welcome to PyQuoridor **\n  Press Enter to start ...")
    while not(quit or victory):
        display(new_pawn, new_fences)
        action = console.prompt_action()
        if action == Action.EXIT:
            quit = True
        else:
            try:
                new_pawn = act(action, new_pawn, new_fences)
            except OutOfBoardException:
                pass
        victory = is_a_victory(new_pawn)
    if victory:
        display(new_pawn, new_fences)
        console.display("** You won **")


def display(pawn, fences):
    console.clear()
    board = get_board(pawn, fences)
    console.display_game(board)


def is_a_victory(pawn):
    return pawn.x == BASE_LINE_SIZE - 1


def act(action, pawn, fences):
    new_pawn = pawn
    if action == Action.RIGHT:
        if is_crossable_right(pawn, fences):
            new_pawn = translate_x(pawn, 2)
        else:
            raise OutOfBoardException("The pawn cannot cross")
    elif action == Action.LEFT:
        if is_crossable_left(pawn, fences):
            new_pawn = translate_x(pawn, -2)
        else:
            raise OutOfBoardException("The pawn cannot cross")
    elif action == Action.DOWN:
        if is_crossable_down(pawn, fences):
            new_pawn = translate_y(pawn, 2)
        else:
            raise OutOfBoardException("The pawn cannot cross")
    elif action == Action.UP:
        if is_crossable_up(pawn, fences):
            new_pawn = translate_y(pawn, -2)
        else:
            raise OutOfBoardException("The pawn cannot cross")
    if is_out_of_board(new_pawn):
        raise OutOfBoardException("The pawn is out of the board")
    return new_pawn
