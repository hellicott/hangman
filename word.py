import random

from alphabet import Alphabet


class Word(object):

    possible_words = ['quack', 'aardvark', 'rhythm']

    def __init__(self, alphabet: Alphabet):
        self.word_to_guess = self.pick_word()
        self.alphabet = alphabet

    def pick_word(self):
        return random.choice(self.possible_words)

    def get_letters(self):
        return set(self.word_to_guess)

    def guess_letter(self, letter):
        self.alphabet.cross_off(letter)
        return letter in self.get_letters()

    def guess_word(self, word):
        return word == self.word_to_guess

    def check_win(self):
        return self.get_letters().issubset(self.alphabet.guessed_letters)

    def get_info(self):
        info_string = "Here's your word: {}\n".format(str(self)) + str(self.alphabet)
        return info_string

    def __len__(self):
        return len(self.word_to_guess)

    def __str__(self):
        hidden_word = self.word_to_guess
        for letter in self.get_letters():
            if letter not in self.alphabet.guessed_letters:
                hidden_word = hidden_word.replace(letter, '_')
        return hidden_word
