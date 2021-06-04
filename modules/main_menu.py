import pygame
from crossword.crossword import run_crossword
from sudoku.sudoku import run_solver, Button
from maze.menu import run
from coloring_graph.main import run_coloring_graph



def run_menu():
    screen = pygame.display.set_mode((800, 600))
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 40)
    screen.fill((247, 255, 163))

    text_1 = font.render("Sudoku solver", 1, (255, 255, 255))
    text_2 = font.render("Maze solver", 1, (255, 255, 255))
    text_3 = font.render("Crossword solver", 1, (255, 255, 255))
    text_4 = font.render("Coloring graph solver", 1, (255, 255, 255))
    text_5 = font.render("Puzzle solver", 1, (255, 255, 255))

    button_1 = Button(screen, (65, 70, 64), 50, 75, 300, 100, text_1, (90, 110))
    button_2 = Button(screen, (65, 70, 64), 450, 75, 300, 100, text_2, (510, 110))
    button_3 = Button(screen, (65, 70, 64), 250, 250, 300, 100, text_3, (280, 285))
    button_4 = Button(screen, (65, 70, 64), 50, 425, 300, 100, text_4, (55, 460))
    button_5 = Button(screen, (65, 70, 64), 450, 425, 300, 100, text_5, (500, 460))

    button_1.draw()
    button_2.draw()
    button_3.draw()
    button_4.draw()
    button_5.draw()
    pygame.display.update()

    flag_1 = True
    flag_2 = True
    while flag_2:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and flag_1:
                if button_1.is_pressed(event):
                    run_solver()
                    flag_1 = False
                elif button_2.is_pressed(event):
                    run('maze/mazefile.txt', 864, 1536, 44)
                    flag_1 = False
                elif button_3.is_pressed(event):
                    run_crossword()
                    flag_1 = False
                elif button_4.is_pressed(event):
                    run_coloring_graph()
                    flag_1 = False
                elif button_5.is_pressed(event):
                    print("not ready")
                    flag_1 = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and not flag_1:
                    flag_2 = False

run_menu()