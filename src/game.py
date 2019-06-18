import math
from copy import deepcopy
from pawn import Orientation, Pawn, translate_x, translate_y
from exception import QuoridorException, OutOfBoardException, UnknownActionException
from functools import reduce
from action import Action
import console
from board import *

from enum import IntEnum

STEP = 2

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
                opponent = new_pawns[get_next_player(player_turn, new_pawns) - 1]
                new_pawn = act(action, new_pawns[player_turn - 1], opponent, new_fences)
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
    return 1 if player_turn + 1 > len(pawns) else player_turn + 1


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


def act(action, pawn, opponent, fences):
    new_pawn = None
    if action == Action.RIGHT:
        new_pawn = move_right(pawn, opponent, fences)
    elif action == Action.LEFT:
        new_pawn = move_left(pawn, opponent, fences)
    elif action == Action.DOWN:
        new_pawn = move_down(pawn, opponent, fences)
    elif action == Action.UP:
        new_pawn = move_up(pawn, opponent, fences)
    else:
        raise UnknownActionException()
    if is_out_of_board(new_pawn):
        raise OutOfBoardException("The pawn is out of the board")
    return new_pawn


def move_right(pawn, opponent, fences):
    if not is_crossable_right(pawn, fences):
        raise OutOfBoardException("The pawn cannot cross")
    if is_opponent_right(pawn, opponent):
        if is_crossable_right(opponent, fences):
            return translate_x(pawn, STEP * 2)
        else:
            raise OutOfBoardException("The pawn cannot cross")
    return translate_x(pawn, STEP)


def move_left(pawn, opponent, fences):
    if not is_crossable_left(pawn, fences):
        raise OutOfBoardException("The pawn cannot cross")
    if is_opponent_left(pawn, opponent):
        if is_crossable_left(opponent, fences):
            return translate_x(pawn, -STEP * 2)
        else:
            raise OutOfBoardException("The pawn cannot cross")
    return translate_x(pawn, -STEP)


def move_up(pawn, opponent, fences):
    if not is_crossable_up(pawn, fences):
        raise OutOfBoardException("The pawn cannot cross")
    if is_opponent_up(pawn, opponent):
        if is_crossable_up(opponent, fences):
            return translate_y(pawn, -STEP * 2)
        else:
            raise OutOfBoardException("The pawn cannot cross")
    return translate_y(pawn, -STEP)


def move_down(pawn, opponent, fences):
    if not is_crossable_down(pawn, fences):
        raise OutOfBoardException("The pawn cannot cross")
    if is_opponent_down(pawn, opponent):
        if is_crossable_down(opponent, fences):
            return translate_y(pawn, STEP * 2)
        else:
            raise OutOfBoardException("The pawn cannot cross")
    return translate_y(pawn, STEP)


def is_opponent_right(pawn, opponent):
    return pawn.x + STEP == opponent.x and pawn.y == opponent.y


def is_opponent_left(pawn, opponent):
    return pawn.x - STEP == opponent.x and pawn.y == opponent.y


def is_opponent_up(pawn, opponent):
    return pawn.x == opponent.x and pawn.y - STEP == opponent.y


def is_opponent_down(pawn, opponent):
    return pawn.x == opponent.x and pawn.y + STEP == opponent.y
