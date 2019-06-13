import unittest
from pawn import Pawn, translate_x, translate_y


class TestPawn(unittest.TestCase):

    def test_translate_x_should_move_the_pawn_to_the_right(self):
        # Given
        expected = Pawn(1, 4)
        # When
        actual = translate_x(Pawn(0, 4), 1)
        # Then
        self.assertEqual(actual, expected, "The pawn should be placed one square after")

    def test_translate_x_should_move_the_pawn_to_the_left(self):
        # Given
        expected = Pawn(-1, 4)
        # When
        actual = translate_x(Pawn(0, 4), -1)
        # Then
        self.assertEqual(actual, expected, "The pawn should be placed one square before")

    def test_translate_y_should_move_the_pawn_to_the_top(self):
        # Given
        expected = Pawn(0, 3)
        # When
        actual = translate_y(Pawn(0, 4), -1)
        # Then
        self.assertEqual(actual, expected, "The pawn should be placed one square on the top")

    def test_translate_y_should_move_the_pawn_to_the_bottom(self):
        # Given
        expected = Pawn(0, 5)
        # When
        actual = translate_y(Pawn(0, 4), 1)
        # Then
        self.assertEqual(actual, expected, "The pawn should be placed one square on the bottom")
