import unittest
import game
from pawn import Pawn


class TestGameMethods(unittest.TestCase):

    def test_init_game_should_add_the_pawn_in_the_center_of_the_base_line(self):
        # Given
        expected = Pawn(0, 4)
        # When
        actual = game.init_game()
        # Then
        self.assertEqual(actual, expected, "The pawn should be placed in the center of his base line")

    def test_get_board_should_add_the_pawn_in_the_center_of_the_base_line(self):
        # Given
        pawn = Pawn(0, 4)
        expected = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
         ]
        # When
        actual = game.get_board(pawn)
        # Then
        self.assertEqual(actual, expected, "In the board, the pawn should be placed in the center of his base line")
