"""
Module for solving the Cryparithetic Puzzle.
Contains Solver class.
"""
from mod_list import ModificatedList
from letter import Letter
from auxiliary import print_final
import pygame


class Solver:
    """
    Solver class. Contains the following methods: __init__, __solve__,
    assign_letter, unassign_letter, is_solved, make_num.
    Static methods: get_letters, check_sum
    """

    def __init__(self, first_word, second_word, sum_word):
        """
        Main method. Is being called when the object of Solver class is created
        :param first_word: first word
        :param second_word: second word
        :param sum_word: summary word
        """
        self.letters_to_assign = Solver.get_letters(first_word, second_word, sum_word)
        self.assigned_letters = ModificatedList()
        self.letters_num = len(self.letters_to_assign)
        self.words = (first_word, second_word, sum_word)

    @staticmethod
    def get_letters(first_word, second_word, sum_word):
        """
        Creates a list of different letters in these words.
        :param first_word: first word
        :param second_word: second word
        :param sum_word: summary word
        :return: list of letters (Letter class)
        """
        letters = []
        for word in [first_word, second_word, sum_word]:
            for letter in word:
                if letter not in letters:
                    letters.append(letter)
        new_letters = [Letter(letter) for letter in letters]

        assert len(letters) <= 10, 'Too much letters'
        return new_letters

    def solve(self):
        """
        Recursive method. Assign every letter a number, the checks arithmetic to see if works
        :return: boolean value
        """
        print(f"""assigned_letters  : {self.assigned_letters}
leters_to_assign: {self.letters_to_assign}""")

        if len(self.letters_to_assign) == 0:
            print('yes')
            return self.is_solved()

        for digit in range(10):
            if self.assign_letter(digit):
                if self.solve():
                    return True
                self.unassign_letter()

    def unassign_letter(self):
        """
        Unassign the digit from letter
        :return: None
        """
        letter = self.assigned_letters.pop()
        self.letters_to_assign.append(letter)

    def assign_letter(self, digit):
        """
        Assign digit to the letter
        :param digit: digit
        :return: boolean value
        """
        letter = self.letters_to_assign[-1]
        if self.assigned_letters.is_containing_digit(digit):
            self.letters_to_assign[-1].set_digit(digit)
            letter = self.letters_to_assign.pop()
            self.assigned_letters.append(letter)
            return True
        return False

    def is_solved(self):
        """
        Method to  check arithmetic to see if works
        :return: boolean value
        """
        first_word_num = self.make_num(self.words[0])
        second_word_num = self.make_num(self.words[1])
        sum_word_num = self.make_num(self.words[2])

        if Solver.check_sum(first_word_num, second_word_num, sum_word_num):
            print_final(self)


            return True

        else:
            print('Once more')

            return False

    def make_num(self, word):
        """
        Method to make a number form the word
        :param word:
        :return: int value of word
        """
        str_num = ''
        for symbol in word:
            for letter in self.assigned_letters:
                if letter._str_value == symbol:
                    str_num += str(letter.get_digit())
        num = int(str_num)
        return num

    @staticmethod
    def check_sum(num_1, num_2, num_3):
        """
        Method to check if the sum of first and second numbers is equal to the third number
        :param num_1: first number
        :param num_2: second number
        :param num_3: third number
        :return: boolean value
        """
        if num_1 + num_2 == num_3:
            return True
        return False




if __name__=='__main__':
    # p = Solver('send', 'more', 'money')
    # p.solve()
    p = Solver('edtg', 'uikf', 'dokim')
    p.solve()


