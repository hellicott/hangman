import os

from display import Display
from alphabet import Alphabet
from word import Word


class Game(object):

    def __init__(self):
        alphabet = Alphabet()
        self.word = Word(alphabet)
        self.display = Display()
        self.wrong_guesses = 0
        self.previous_result = ""

    @staticmethod
    def menu():
        print(" 1 | Guess a Letter")
        print(" 2 | Guess a Word")
        print("Enter anything else to give up")
        choice = input("Enter the number of your choice> ")
        return choice

    @staticmethod
    def clear_screen():
        _ = os.system('cls')

    def play(self):
        while True:
            self.clear_screen()
            self.print_display()
            choice = self.menu()
            if choice == '1':
                self.guess_letter()
            elif choice == '2':
                if self.guess_word():
                    self.win()
                    break
            else:
                break
            if self.word.check_win():
                self.win()
                break

    def win(self):
        print(self.previous_result)
        print("YAY!")

    def print_display(self):
        print(self.previous_result)
        print(self.display.get_board(self.wrong_guesses))
        print(self.word.get_info())
        print("-"*100)

    def guess_letter(self):
        letter_guessed = input("Guess a letter> ")
        result = self.word.guess_letter(letter_guessed)
        if result:
            self.previous_result = "Nice one, that was right"
            return True
        else:
            self.previous_result = "Unlucky, that was not in the word"
            self.wrong_guesses += 1
            return False

    def guess_word(self):
        word_guessed = input("Guess a word> ")
        result = self.word.guess_word(word_guessed)
        if result:
            self.previous_result = "Nice one, you guessed the word"
            return True
        else:
            self.previous_result = "Unlucky, that was not the word"
            self.wrong_guesses += 1
            return False


def main():
    game = Game()
    game.play()


main()