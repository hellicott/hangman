from unittest import TestCase
from display import Display


class TestDisplay(TestCase):
    def test_get_board_returns_string(self):
        # arrange
        display = Display()
        # act
        lives_display = display.get_board(0)
        # assert
        assert type(lives_display) == str
