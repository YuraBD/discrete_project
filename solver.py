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
        self.set_up()


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
        self.draw_numbers()

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


    def set_up(self):

        pygame.init()
        self.myfont = pygame.font.SysFont('timesnewroman',  25)
        colors = [(218, 247, 166),( 255, 195, 0 )]
        pygame.font.init()
        self.screen = pygame.display.set_mode((100*self.letters_num, 50))
        pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING")
        self.screen.fill((49,150,100))
        pygame.display.flip()
        for i in range(self.letters_num):
            pygame.draw.rect(self.screen, colors[i%2], pygame.Rect(100*i , 0 , 100, 50))
            pygame.display.flip()

        for i in range(self.letters_num):
            text = str(self.letters_to_assign[i])+ ':'
            textsurface = self.myfont.render(text, False, (0, 0, 0))
            self.screen.blit(textsurface, (15+ i*100, 12))

            pygame.display.flip()

    def draw_numbers(self):
        colors = [(218, 247, 166), (255, 195, 0)]
        numbers_len = len(self.assigned_letters)
        for i in range(10):
            pygame.draw.rect(self.screen, colors[i%2], pygame.Rect(100*i+50 , 0 , 50, 50))
            pygame.display.flip()
        for i in range(numbers_len):
            text =str(self.assigned_letters[i].get_digit())
            textsurface = self.myfont.render(text, False, (0, 0, 0))
            self.screen.blit(textsurface, (65+ i*100, 12))

            pygame.display.flip()








if __name__=='__main__':
    p = Solver('send', 'more', 'money')
    p.solve()
    # p = Solver('send', 'more', 'money')
    # p.solve()

    # pygame.font.init()
    # screen = pygame.display.set_mode((300, 300))
    # pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING")
    # screen.fill((49, 150, 100))
    # pygame.display.flip()
    # for i in range(2):
    #     pygame.draw.line(screen, (100, 100, 100), (10, 10), (50, 50), 10)
    # pygame.font.init()
    # screen = pygame.display.set_mode((1000, 50))
    # pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING")
    # screen.fill((49, 150, 100))
    # pygame.display.flip()
    # a=0
    # i=0
    # while True:
    #     pygame.draw.rect(screen, (255, a, 51), pygame.Rect(100*i , 0 , 100, 50))
    #     pygame.display.flip()
    #     a+=2
    #     if a>255:
    #         a=0
    #     i+=1





