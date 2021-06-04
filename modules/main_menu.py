import pygame
from sudoku.sudoku import run_solver, Button
from maze.menu import run
from coloring_graph.main import run_coloring_graph
from crossword.crossword import run_crossword


def run_menu():
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont("comicsans", 40)
    screen.fill((247, 255, 163))

    text_1 = font.render("Sudoku solver", 1, (255, 255, 255))
    text_2 = font.render("Maze solver", 1, (255, 255, 255))
    text_3 = font.render("Crossword solver", 1, (255, 255, 255))
    text_4 = font.render("Coloring graph solver", 1, (255, 255, 255))
    text_5 = font.render("Puzzle solver", 1, (255, 255, 255))

run('maze/mazefile.txt', 1080, 1920, 44)