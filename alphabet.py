class Alphabet(object):
    def __init__(self):
        self.letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.guessed_letters = set()

    def cross_off(self, letter):
        self.guessed_letters.add(letter.lower())

    def already_guessed(self, letter):
        if letter in self.guessed_letters:
            return True
        return False

    def __str__(self):
        letters_not_guessed = [x if x not in self.guessed_letters else ' ' for x in self.letters]
        num = 52
        space = 52 - (len(self.guessed_letters)*2 - 1)
        print(space)
        alphabet_string = ['╔' + '═' * num + '╗\n'
                           '║' + " ".join(letters_not_guessed) + ' ║\n'
                           '╠' + '═' * num + '╣\n'
                           '║' + "Already guessed letters:" + " " * 28 + '║\n'
                           '║' + " ".join(self.guessed_letters) + " " * space + '║\n'
                           '╚' + '═' * num + '╝\n']
        return str(alphabet_string[0])
