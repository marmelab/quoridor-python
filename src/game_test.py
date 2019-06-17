import unittest
import game
from pawn import Pawn
from board import FENCE_SIZE, Direction
from exception import OutOfBoardException, UnknownActionException
from action import Action


class TestGame(unittest.TestCase):

    def test_init_game_should_add_the_pawn_in_the_center_of_the_base_line(self):
        # Given
        expected = [Pawn(0, 8), Pawn(16, 8)]
        # When
        actual = game.init_game()
        # Then
        self.assertEqual(actual, expected, "The pawn should be placed in the center of his base line")

    def test_act_should_move_the_pawn_one_square_to_the_top(self):
        # Given
        pawn = Pawn(0, 8)
        fences = [[Direction.NO for i in range(FENCE_SIZE)] for j in range(FENCE_SIZE)]
        expected = Pawn(0, 6)
        # When
        actual = game.act(Action.UP, pawn, fences)
        # Then
        self.assertEqual(actual, expected, "The pawn should move one square to the top")

    def test_act_should_move_the_pawn_one_square_to_the_bottom(self):
        # Given
        pawn = Pawn(0, 8)
        fences = [[Direction.NO for i in range(FENCE_SIZE)] for j in range(FENCE_SIZE)]
        expected = Pawn(0, 10)
        # When
        actual = game.act(Action.DOWN, pawn, fences)
        # Then
        self.assertEqual(actual, expected, "The pawn should move one square to the bottom")

    def test_act_should_move_the_pawn_one_square_to_the_right(self):
        # Given
        pawn = Pawn(0, 8)
        expected = Pawn(2, 8)
        # When
        actual = game.act(Action.RIGHT, pawn)
        # Then
        self.assertEqual(actual, expected, "The pawn should move one square to the right")

    def test_act_should_move_the_pawn_one_square_to_the_right(self):
        # Given
        pawn = Pawn(2, 8)
        fences = [[Direction.NO for i in range(FENCE_SIZE)] for j in range(FENCE_SIZE)]
        expected = Pawn(0, 8)
        # When
        actual = game.act(Action.LEFT, pawn, fences)
        # Then
        self.assertEqual(actual, expected, "The pawn should move one square to the left")

    def test_act_should_raise_exception_with_unknown_action(self):
        # Given
        pawn = Pawn(2, 8)
        fences = [[Direction.NO for i in range(FENCE_SIZE)] for j in range(FENCE_SIZE)]
        # When Then
        self.assertRaises(UnknownActionException, game.act, Action.UNKNOWN, pawn, fences)

    def test_act_should_raise_the_exception_when_moving_out_of_the_board(self):
        # Given
        pawn = Pawn(0, 8)
        fences = [[Direction.NO for i in range(FENCE_SIZE)] for j in range(FENCE_SIZE)]
        # When Then
        self.assertRaises(OutOfBoardException, game.act, Action.LEFT, pawn, fences)

    def test_is_a_victory_should_be_ok_the_pawn_reaches_the_opposite_base_line(self):
        # Given
        pawns = [Pawn(16, 4)]
        # When
        actual = game.is_a_victory(pawns)
        # Then
        self.assertTrue(actual, "The pawn should won, it reached the opponent base line")

    def test_is_a_victory_should_not_be_ok_the_pawn_is_on_the_board(self):
        # Given
        pawns = [Pawn(10, 8)]
        # When
        actual = game.is_a_victory(pawns)
        # Then
        self.assertFalse(actual, "The game should continue, the pawn is on the board")
