from os import curdir
import pygame


class Button:
    """Represent button"""
    def __init__(self, screen, color, x, y, width, height, text, text_coords):
        """Initialize button2"""
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_coords = text_coords

    def draw(self):
        """Draw a button"""
        pygame.draw.rect(self.screen, self.color,
                        (self.x, self.y, self.width, self.height))
        self.screen.blit(self.text, self.text_coords)

    def is_pressed(self, event):
        """Check if button is pressed"""
        pos = pygame.mouse.get_pos()
        return self.x <= pos[0] <= self.x + self.width and\
                self.y <= pos[1] <= self.y + self.height


class Cursor:
    """Represent cursor"""
    def __init__(self):
        """Initializw cursor"""
        self.row = 0
        self.col = 0

    def draw(self, screen, dif):
        """Draw cursor"""
        for i in range(2):
            pygame.draw.line(screen, (255, 0, 0), (self.col * dif-3, (self.row + i)*dif),
                            (self.col * dif + dif + 3, (self.row + i)*dif), 7)
            pygame.draw.line(screen, (255, 0, 0), ( (self.col + i)* dif, self.row * dif ),
                            ((self.col + i) * dif, self.row * dif + dif), 7)


class Board:
    """Represent board"""
    def __init__(self):
        """Initialize board"""
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.cursor = Cursor()
        pygame.font.init()
        self.font = pygame.font.SysFont("comicsans", 40)
        self.dif = 500/9
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Sudoku solver")


    def from_file(self, path):
        """Read board from file"""
        with open(path, 'r') as grid_file:
            grid = grid_file.readlines()
        self.grid = [[int(num) for num in list(line.strip())] for line in grid]

    def find_empty_location(self):
        """Find entry in the grid that is not used
        Return False if there are no possible entries"""
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    self.cursor.row = row
                    self.cursor.col = col
                    return True
        return False

    def used_in_row(self, num):
        """Check if given number was used in current row"""
        for col in range(9):
            if self.grid[self.cursor.row][col] == num:
                return True
        return False

    def used_in_col(self, num):
        """Check if given number was used in current column"""
        for row in range(9):
            if self.grid[row][self.cursor.col] == num:
                return True
        return False

    def used_in_box(self, num):
        """Check if given number was used in current 3x3 box"""
        b_row = self.cursor.row - self.cursor.row % 3
        b_col = self.cursor.col - self.cursor.col % 3
        for row in range(3):
            for col in range(3):
                if self.grid[b_row + row][b_col + col] == num:
                    return True
        return False

    def check_location(self, num):
        """Check if it is possible to assign number to a current position"""
        return not self.used_in_row(num) and\
               not self.used_in_col(num) and\
               not self.used_in_box(num)

    def draw(self):
        """Draw game board"""
        self.screen.fill((247, 255, 163))
        for row in range(9):
            for col in range (9):
                if self.grid[row][col]!= 0:
                    pygame.draw.rect(self.screen, (247, 153, 35),
                                    (col * self.dif, row * self.dif, self.dif + 1, self.dif + 1))
                    text = self.font.render(str(self.grid[row][col]), 1, (0, 0, 0))
                    self.screen.blit(text, (col * self.dif + 20, row * self.dif + 15))
        for i in range(10):
            if i % 3 == 0 :
                thick = 7
            else:
                thick = 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * self.dif), (500, i * self.dif), thick)
            pygame.draw.line(self.screen, (0, 0, 0), (i * self.dif, 0), (i * self.dif, 500), thick)

    def solve(self, animation = False):
        """Solve sudoku"""
        if not self.find_empty_location():
            return True
        row = self.cursor.row
        col = self.cursor.col
        for num in range(10):
            if self.check_location(num):
                self.grid[self.cursor.row][self.cursor.col] = num
                if animation:
                    self.draw()
                    self.cursor.draw(self.screen, self.dif)
                    pygame.display.update()
                    pygame.time.delay(20)
                if self.solve(animation):
                    return True
                self.cursor.row = row
                self.cursor.col = col
                if animation:
                    self.draw()
                    self.cursor.draw(self.screen, self.dif)
                    pygame.display.update()
                    pygame.time.delay(20)
                self.grid[self.cursor.row][self.cursor.col] = 0
        return False


def run_solver():
    """Run sudoku solver"""
    board = Board()
    board.from_file("sudoku/sudoku.txt")
    board.screen.fill((247, 255, 163))

    text_1 = board.font.render("Solve with animation", 1, (255, 255, 255))
    button_1 = Button(board.screen, (65, 70, 64), 60, 60, 380, 130, text_1, (100, 112))
    text_2 = board.font.render("Solve without animation", 1, (255, 255, 255))
    button_2 = Button(board.screen, (65, 70, 64), 60, 310, 380, 130, text_2, (80, 362))
    button_1.draw()
    button_2.draw()
    pygame.display.update()

    flag_1 = True
    flag_2 = True
    while flag_2:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and flag_1:
                if button_1.is_pressed(event):
                    board.solve(True)
                    flag_1 = False
                elif button_2.is_pressed(event):
                    board.solve()
                    board.screen.fill((247, 255, 163))
                    board.draw()
                    pygame.display.update()
                    flag_1 = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and not flag_1:
                    flag_2 = False


if __name__ == "__main__":
    run_solver()