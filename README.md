# hangman
An example solution of a command line hangman game. I used this challenge to help teach classes and how they work to a person new to programming

---
## Class and method outlines

#### alphabet.py 
```
class Alphabet(object):
    def __init__(self):
        self.letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.guessed_letters = set()

    def cross_off(self, letter):
        # add to guessed letters

    def already_guessed(self, letter):
        # return true/false of whether in guessed letters

    def __str__(self):
        # return string
```
#### display.py
```
class Display(object):
    def __init__(self):
        self.boards = []  # list of boards as strings
    
    def get_board(self, num):
        # return a board
```
#### word.py
```
class Word(object):

    possible_words = ['quack', 'aardvark', 'rhythm']

    def __init__(self, alphabet: Alphabet):
        self.word_to_guess = self.pick_word()
        self.alphabet = alphabet

    def pick_word(self):
        # return random word from list

    def get_letters(self):
        # return set of letters in words (no repeats)

    def guess_letter(self, letter):
        # cross off letter
        # return true/false of whether in word

    def guess_word(self, word):
        # return true/false of whether word is correct

    def check_win(self):
        # return true/false of whether all letters guessed

    def get_info(self):
        # return string of word in 'hidden' form, list of guessed letters, etc.

    def __len__(self):
        # return length of word to guess

    def __str__(self):
        # return hidden form of word to guess (e.g. '_ _ _' instead of 'BUG')
```
#### hangman.py
```
class Game(object):

    def __init__(self):
        alphabet = Alphabet()
        self.word = Word(alphabet)
        self.display = Display()
        self.wrong_guesses = 0
        self.previous_result = ""

    @staticmethod
    def menu():
        # print menu
        # return user input of choice

    @staticmethod
    def clear_screen():
        _ = os.system('cls')

    def play(self):
        # loop methods until win or lose

    def win(self):
        # print winning message

    def print_display(self):
        # print board, letters guessed, word, etc.

    def guess_letter(self):
        # get input
        # return true/false for whether in word

    def guess_word(self):
        # get input
        # return true/false for whether correct guess


def main():
    game = Game()
    game.play()


main()
```