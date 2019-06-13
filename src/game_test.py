import unittest
import game
from pawn import Pawn
from exception import OutOfBoardException


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

    def test_get_board_should_add_the_pawn_in_the_top_left_of_the_board(self):
        # Given
        pawn = Pawn(0, 0)
        expected = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
         ]
        # When
        actual = game.get_board(pawn)
        # Then
        self.assertEqual(actual, expected, "In the board, the pawn should be placed in the top left of the board")

    def test_get_board_should_add_the_pawn_in_the_bottom_left_of_the_board(self):
        # Given
        pawn = Pawn(0, 8)
        expected = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
         ]
        # When
        actual = game.get_board(pawn)
        # Then
        self.assertEqual(actual, expected, "In the board, the pawn should be placed in the bottom left of the board")

    def test_get_board_should_add_the_pawn_in_the_top_right_of_the_board(self):
        # Given
        pawn = Pawn(8, 0)
        expected = [
            [0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
         ]
        # When
        actual = game.get_board(pawn)
        # Then
        self.assertEqual(actual, expected, "In the board, the pawn should be placed in the top right of the board")

    def test_get_board_should_add_the_pawn_in_the_bottom_right_of_the_board(self):
        # Given
        pawn = Pawn(8, 8)
        expected = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1],
         ]
        # When
        actual = game.get_board(pawn)
        # Then
        self.assertEqual(actual, expected, "In the board, the pawn should be placed in the bottom right of the board")

    def test_get_board_should_throw_exception_if_pawn_x_is_greater_than_the_size_of_the_board(self):
        # Given
        pawn = Pawn(9, 4)
        # When Then
        self.assertRaises(OutOfBoardException, game.get_board, pawn)
    
    def test_get_board_should_throw_exception_if_pawn_y_is_greater_than_the_size_of_the_board(self):
        # Given
        pawn = Pawn(4, 9)
        # When Then
        self.assertRaises(OutOfBoardException, game.get_board, pawn)

    def test_get_board_should_throw_exception_if_pawn_x__si_less_than_the_board(self):
        # Given
        pawn = Pawn(-1, 0)
        # When Then
        self.assertRaises(OutOfBoardException, game.get_board, pawn)

    def test_get_board_should_throw_exception_if_pawn_y__si_less_than_the_board(self):
        # Given
        pawn = Pawn(0, -1)
        # When Then
        self.assertRaises(OutOfBoardException, game.get_board, pawn)