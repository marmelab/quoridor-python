import math
from copy import deepcopy
from pawn import Orientation, Pawn, translate_x, translate_y
from exception import QuoridorException, OutOfBoardException, UnknownActionException
from functools import reduce
from action import Action
import console
from board import *

from enum import IntEnum


class State(IntEnum):
    RUNNING = 0,
    VICTORY = 1,
    QUIT = 2,


def init_game():
    center = math.floor(BASE_LINE_SIZE / 2)
    return [Pawn(0, center, Orientation.WEST), Pawn(BASE_LINE_SIZE - 1, center, Orientation.EAST)]


def progress(pawns):
    new_fences = build()
    player_turn = 1
    state = State.RUNNING
    console.clear()
    console.prompt("\n *** Welcome to PyQuoridor ***\n  Press Enter to start ...")
    new_pawns = deepcopy(pawns)
    while state == State.RUNNING:
        display(new_pawns, new_fences)
        action = console.prompt_action(player_turn)
        if action == Action.EXIT:
            state = State.QUIT
        else:
            try:
                new_pawns = deepcopy(new_pawns)
                new_pawn = act(action, new_pawns[player_turn - 1], new_fences)
                new_pawns[player_turn - 1] = new_pawn
                if is_a_victory(new_pawn):
                    state = State.VICTORY
                else:
                    player_turn = get_next_player(player_turn, new_pawns)
            except QuoridorException:
                pass
    if state == State.VICTORY:
        display(new_pawns, new_fences)
        console.display("\n *** Player # " + str(player_turn) + " won ***\n")


def get_next_player(player_turn, pawns):
    if player_turn + 1 > len(pawns):
        return 1
    return player_turn + 1


def display(pawns, fences):
    console.clear()
    board = get_board(pawns, fences)
    console.display_game(board)


def is_a_victory(pawn):
    victory: None
    if pawn.goal == Orientation.EAST:
        victory = pawn.x == 0
    elif pawn.goal == Orientation.WEST:
        victory = pawn.x == BASE_LINE_SIZE - 1
    else:
        raise QuoridorException("This version supports only 2 players")
    return victory


def act(action, pawn, fences):
    new_pawn = None
    if action == Action.RIGHT:
        new_pawn = move_right(pawn, fences)
    elif action == Action.LEFT:
        new_pawn = move_left(pawn, fences)
    elif action == Action.DOWN:
        new_pawn = move_down(pawn, fences)
    elif action == Action.UP:
        new_pawn = move_up(pawn, fences)
    else:
        raise UnknownActionException()
    if is_out_of_board(new_pawn):
        raise OutOfBoardException("The pawn is out of the board")
    return new_pawn


def move_right(pawn, fences):
    if not is_crossable_right(pawn, fences):
        raise OutOfBoardException("The pawn cannot cross")
    return translate_x(pawn, 2)


def move_left(pawn, fences):
    if not is_crossable_left(pawn, fences):
        raise OutOfBoardException("The pawn cannot cross")
    return translate_x(pawn, -2)


def move_up(pawn, fences):
    if not is_crossable_up(pawn, fences):
        raise OutOfBoardException("The pawn cannot cross")
    return translate_y(pawn, -2)


def move_down(pawn, fences):
    if not is_crossable_down(pawn, fences):
        raise OutOfBoardException("The pawn cannot cross")
    return translate_y(pawn, 2)
