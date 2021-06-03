from mod_list import ModificatedList
from letter import Letter
import pygame
class Solver:
    def __init__(self, first_word, second_word, sum_word):
        self.letters_to_assign = Solver.get_letters(first_word, second_word, sum_word)
        # self.assigned_letters = ModificatedDict()
        self.assigned_letters = ModificatedList()
        self.letters_num = len(self.letters_to_assign)
    @staticmethod
    def get_letters(first_word, second_word, sum_word):
        letters = []
        for word in [first_word, second_word, sum_word]:
            for letter in word:
                if letter not in letters:
                    letters.append(letter)
        new_letters = [Letter(letter) for letter in letters]

        assert len(letters) <= 10, 'Too much letters'
        return new_letters

    def solve(self):
        print(f"""assigned_letters  : {self.assigned_letters}
leters_to_assign: {self.letters_to_assign}""")

        if len(self.letters_to_assign) == 0:
            print('yes')
            return self.is_solved()

            # solve(letters_to_assign, assigned_letters)
        for digit in range(9):
            if self.assign_letter(digit):
                if self.solve():
                    return True
                self.unassign_letter()


    def unassign_letter(self):
        letter = self.assigned_letters.pop()
        self.letters_to_assign.append(letter)


    def assign_letter(self, digit):
        letter =self.letters_to_assign[-1]
        if self.assigned_letters.is_containing_digit(digit):
            self.letters_to_assign[-1].set_digit(digit)
            letter = self.letters_to_assign.pop()
            self.assigned_letters.append(letter)
            return True
        return False









    # def assign_letter(self, digit):
    #     letter = self.letters_to_assign[-1]
    #     print(f'letter.checked {self.letters_to_assign[-1].checked}')
    #     if self.assigned_letters.is_not_contained(digit) and digit not in letter.checked:
    #         self.assigned_letters[letter] = digit
    #         self.letters_to_assign[-1].add_to_checked(digit)
    #         self.letters_to_assign[-1].counter += 1
    #         print(self.letters_to_assign[-1].checked)
    #         self.letters_to_assign.pop()
    #
    #         return True
    #
    #     return False
    #
    def is_solved(self):
        first_word_num = self.make_num('send')
        second_word_num = self.make_num('more')
        sum_word_num = self.make_num('money')
        # if self.assigned_letters[-1].digit == 7 and self.assigned_letters[-3].digit == 2:
        #     print('done')
        #     return True

        if Solver.check_sum(first_word_num, second_word_num, sum_word_num):
            print('done')
            return True

        else:
            print('not done')

            return False

    def make_num(self, word):
        str_num = ''
        for symbol in word:
            for letter in self.assigned_letters:
                if letter._str_value==symbol:
                    str_num+=str(letter.get_digit())
        num = int(str_num)
        return num

    @staticmethod
    def check_sum(num_1, num_2, num_3):
        if num_1 + num_2 == num_3:
            return True
        return False



p = Solver('send', 'more', 'money')
p.solve()