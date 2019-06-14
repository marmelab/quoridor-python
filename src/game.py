import math
from pawn import Pawn, translate_x, translate_y
from exception import OutOfBoardException
from functools import reduce
from action import Action
import console
from board import build, get_board, BASE_LINE_SIZE, is_out_of_board


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
                new_pawn = act(action, new_pawn)
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


def act(action, pawn):
    new_pawn = pawn
    if action == Action.RIGHT:
        new_pawn = translate_x(pawn, 2)
    elif action == Action.LEFT:
        new_pawn = translate_x(pawn, -2)
    elif action == Action.DOWN:
        new_pawn = translate_y(pawn, 2)
    elif action == Action.UP:
        new_pawn = translate_y(pawn, -2)
    if (is_out_of_board(new_pawn)):
        raise OutOfBoardException("The pawn is out of the board")
    return new_pawn
