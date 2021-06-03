"""
Module for the crossword solving algorithm.
"""
import time
import pygame

pygame.init()
screen = pygame.display.set_mode((765, 510))

PATH = "crossword.txt"

def show_matrix(lst):
    """
    Function is used for representing the current matrix.
    """
    x, y = 0, 0
    for line in lst:
        for letter in line:
            color = 'green'
            if letter == '-':
                letter = ''
            if letter == '+':
                letter = ''
                color = 'white'
            pygame.draw.rect(screen, color, pygame.Rect(x, y, 50, 50))
            font = pygame.font.SysFont(None, 40)
            img = font.render(letter, True, 'blue')
            screen.blit(img, (x + 19, y + 12))
            x += 51
        y += 51
        x = 0
    pygame.display.update()

class Crossword:
    """
    Class for representing crosswords.
    """
    def __init__(self, file_path):
        """
        Initialize crossword.
        """
        self.grid, self.words = self.read_from_file(file_path)
        self.possible_positions = self.possible_positions()

    def read_from_file(self, file_path):
        """
        Read txt file and return the grid and the list of words that
        are needed to solve the crossword.
        The first part of the file should contain 
        '-'(position for the letter) and 
        '+'(space that should not be filled)
        Then there is an empty line that indicates 
        that it is time to read the words.
        """
        grid = []
        with open(file_path, 'r', encoding='utf-8') as inp_file:
            while True:
                line = inp_file.readline().split()
                if not line:
                    break
                grid.append(line)

            words = []
            line = inp_file.readline().split()
            while True:
                line = inp_file.readline().strip()
                if not line:
                    break
                words.append(line)
        return grid, words

    def possible_positions(self):
        """
        Find all possible positions for the given words.
        Return a list of the positions that should be filled with words.
        Each word position has it's axis, coordinates (x, y), length 
        and status (if there is already a word).
        """
        i = 0
        j = 0
        positions = []
        num_cols = len(self.grid[0])
        num_rows = len(self.grid)
        for row in self.grid:
            counter = 0
            for letter in row:
                if letter == '-' and not j == num_cols-1:
                    counter += 1
                elif counter > 2:
                    if j == num_cols-1:
                        positions.append(['h', (i, j-counter), counter+1, True])
                    else:
                        positions.append(['h', (i, j-counter), counter, True])
                    counter = 0
                else:
                    counter = 0
                j += 1
            i += 1
            j = 0

        i = 0
        j = 0
        for col in range(num_cols):
            counter = 0
            for row in self.grid:
                if row[col] == '-' and not i == num_rows-1:
                    counter += 1
                elif counter > 2:
                    if i == num_rows-1:
                        positions.append(['v', (i-counter, j), counter+1, True])
                    else:
                        positions.append(['v', (i-counter, j), counter, True])
                    counter = 0
                else:
                    counter = 0
                i += 1
            j += 1
            i = 0
            counter = 0

        return positions

    def solver(self):
        """
        Function that solves the crossword.
        There is given a list of words and a grid.
        The task is to fill the gaps with those words 
        using backtracking algorithm.
        Return a list that contains the final (solved) crossword.
        """
        matrix = self.grid
        words = self.words


        def solve_crossword(matrix, words, ind):
            """
            Recursive function that is used for backtracking.
            """

            show_matrix(matrix)
            time.sleep(0.5)


            def can_place_h(matrix, current, i, j):
                """
                Check if it's possible to place the current word in 
                the position with the given coordinates horizontally.
                """
                if j-1 >= 0 and matrix[i][j-1] != '+':
                    return False
                if j+len(current) < len(matrix[0]) and matrix[i][j + len(current)] != "+":
                    return False
                for x in range(len(current)):
                    if x+j >= num_cols:
                        return False
                    if matrix[i][x+j] == '-' or matrix[i][x+j] == current[x]:
                        continue
                    else:
                        return False
                return True

            def can_place_v(matrix, current, i, j):
                """
                Check if it's possible to place the current word in 
                the position with the given coordinates vertically.
                """
                if i-1 >= 0 and matrix[i-1][j] != '+':
                    return False
                if i+len(current) < num_rows and matrix[i+len(current)][j] != '+':
                    return False
                for x in range(len(current)):
                    if x+i >= num_rows:
                        return False
                    if matrix[x+i][j] == '-' or matrix[x+i][j] == current[x]:
                        continue
                    else:
                        return False
                return True

            def place_h(matrix, current, i, j):
                """
                Place the current word in the position horizontally.
                """
                b = [None]*num_cols
                for k in range(len(current)):
                    if matrix[i][j+k] == '-':
                        b[k] = True
                        matrix[i][j+k] = current[k]
                    else:
                        b[k] = False
                return b

            def place_v(matrix, current, i, j):
                """
                Place the current word in the position vertically.
                """
                b = [None]*num_rows
                for k in range(len(current)):
                    if matrix[i+k][j] == '-':
                        b[k] = True
                        matrix[i+k][j] = current[k]
                    else:
                        b[k] = False
                return b

            def unplace_h(matrix, b, i, j):
                """
                Undo placing the word in the position (horizonally).
                """
                for k in range(len(b)):
                    if b[k]:
                        matrix[i][j+k] = '-'

            def unplace_v(matrix, b, i, j):
                """
                Undo placing the word in the position (vertically).
                """
                for k in range(len(b)):
                    if b[k]:
                        matrix[i+k][j] = '-'

            if ind == len(words):
                res = []
                for line in self.grid:
                    row_lst = []
                    for item in line:
                        row_lst.append(item)
                    res.append(row_lst)
                lst.append(res)
                return

            current = words[ind]
            num_rows = len(matrix)
            num_cols = len(matrix[0])
            for i in range(num_rows):
                for j in range(num_cols):
                    if matrix[i][j] == '-' or matrix[i][j] == current[0]:
                        for _ in range(2):
                            if can_place_h(matrix, current, i, j):
                                b = place_h(matrix, current, i, j)
                                solve_crossword(matrix, words, ind+1)
                                unplace_h(matrix, b, i, j)
                                break
                            elif can_place_v(matrix, current, i, j):
                                b = place_v(matrix, current, i, j)
                                solve_crossword(matrix, words, ind+1)
                                unplace_v(matrix, current, i, j)
                                break
                            else:
                                current = current[::-1]


        lst = []
        solve_crossword(matrix, words, 0)
        show_matrix(lst[0])
        time.sleep(5)
        return lst


if __name__ == "__main__":
    crossword = Crossword(PATH)
    crossword.solver()
