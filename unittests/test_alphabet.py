from unittest import TestCase
from alphabet import Alphabet


class TestAlphabet(TestCase):
    def test_new_alphabet_contains_26_letters(self):
        # arrange
        # act
        alphabet = Alphabet()
        # assert
        assert len(alphabet.letters) == 26

    def test_cross_off_adds_guessed_letter_to_list_of_guessed_letters(self):
        # arrange
        alphabet = Alphabet()
        letter = "a"
        # act
        alphabet.cross_off(letter)
        # assert
        assert letter in alphabet.guessed_letters

    def test_cross_off_adds_lowercase_guessed_letter_to_list_of_guessed_letters(self):
        # arrange
        alphabet = Alphabet()
        letter = "A"
        # act
        alphabet.cross_off(letter)
        # assert
        assert "a" in alphabet.guessed_letters

    def test_already_guessed_returns_false_if_letter_not_guessed(self):
        # arrange
        alphabet = Alphabet()
        letter = "h"
        alphabet.cross_off(letter)
        # act
        result = alphabet.already_guessed("g")
        # assert
        assert result is False

    def test_already_guessed_returns_true_if_letter_guessed(self):
        # arrange
        alphabet = Alphabet()
        letter = "h"
        alphabet.cross_off(letter)
        # act
        result = alphabet.already_guessed("h")
        # assert
        assert result is True
