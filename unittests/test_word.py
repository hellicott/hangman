from unittest import TestCase, mock
from word import Word
from alphabet import Alphabet


class TestWord(TestCase):
    def test_pick_word_returns_a_string_longer_than_3_letters(self):
        # arrange
        alphabet = mock.create_autospec(Alphabet)
        word = Word(alphabet)
        # act
        chosen_word = word.pick_word()

        # assert
        assert chosen_word in word.possible_words

    def test_get_letters_returns_set_of_letters_in_word(self):
        # arrange
        alphabet = mock.create_autospec(Alphabet)
        word = Word(alphabet)
        word.word_to_guess = "quack"
        # act
        letter_set = word.get_letters()
        # assert
        assert letter_set == {"q", "u", "a", "c", "k"}

    def test_get_letters_returns_set_of_letters_in_word_with_repeated_letters(self):
        # arrange
        alphabet = mock.create_autospec(Alphabet)
        word = Word(alphabet)
        word.word_to_guess = "aardvark"
        # act
        letter_set = word.get_letters()
        # assert
        assert letter_set == {"a", "r", "d", "v", "k"}

    def test_str_representation_does_not_show_hidden_letters(self):
        # arrange
        alphabet = Alphabet()
        word = Word(alphabet)
        word.word_to_guess = "aardvark"
        word.guess_letter("a")
        # act
        hidden_word = str(word)
        # assert
        assert hidden_word == "aa___a__"
