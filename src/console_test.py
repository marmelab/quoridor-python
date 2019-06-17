import unittest
from action import Action
from console import commands, get_action


class TestConsole(unittest.TestCase):

    def test_get_action_should_return_the_right_input(self):
        # Given
        expected = Action.DOWN
        # When
        actual = get_action("2")
        # Then
        self.assertEqual(actual, expected, "The action should be down")

    def test_get_action_should_return_the_default_action(self):
        # Given
        expected = Action.UNKNOWN
        # When
        actual = get_action("ze")
        # Then
        self.assertEqual(actual, expected, "The action should be unknown")
