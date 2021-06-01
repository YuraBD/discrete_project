import pygame
from sudoku_solver import find_empty_location, check_location_is_safe

pygame.font.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Sudoku solver")

x = 0
y = 0
dif = 500 / 9
val = 0
grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

font = pygame.font.SysFont("comicsans", 40)


def get_cord(pos):
    '''Get coord of current position'''
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif


def draw_box():
    '''Highlight the cell selected'''
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (y * dif-3, (x + i)*dif), (y * dif + dif + 3, (x + i)*dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ( (y + i)* dif, x * dif ), ((y + i) * dif, x * dif + dif), 7)


def draw():
    '''Function to draw required lines for making Sudoku grid'''
    for i in range (9):
        for j in range (9):
            if grid[i][j]!= 0:
  
                pygame.draw.rect(screen, (247, 153, 35), (j * dif, i * dif, dif + 1, dif + 1))

                text = font.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text, (j * dif + 20, i * dif + 15))
    for i in range(10):
        if i % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)


def solve_sudoku_without_animation(grid):
    '''Solve given grid without animation'''
    pos = [0, 0]
 
    if(not find_empty_location(grid, pos)):
        return True

    row = pos[0]
    col = pos[1]

    for num in range(1, 10):
         
        if(check_location_is_safe(grid,
                          row, col, num)):
             
            grid[row][col]= num
            y = col
            if(solve_sudoku_without_animation(grid)):
                return True
 
            grid[row][col] = 0
            
    return False

def solve_sudoku_with_animation(grid):
    '''Solve given grid with animation'''
    pos = [0, 0]
    if(not find_empty_location(grid, pos)):
        return True

    row = pos[0]
    col = pos[1]

    for num in range(1, 10):
         
        if(check_location_is_safe(grid,
                          row, col, num)):

            grid[row][col]= num
            global x, y
            x = row
            y = col
            screen.fill((247, 255, 163))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if(solve_sudoku_with_animation(grid)):
                return True
            screen.fill((247, 255, 163))
          
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            grid[row][col] = 0

    return False


def run():
    '''Run sudoku solver'''
    screen.fill((247, 255, 163))


    pygame.draw.rect(screen, (65, 70, 64), (60, 60, 380, 130))
    text = font.render("Solve with animation", 1, (255, 255, 255))
    screen.blit(text, (100, 112))

    pygame.draw.rect(screen, (65, 70, 64), (60, 310, 380, 130))
    text = font.render("Solve without animation", 1, (255, 255, 255))
    screen.blit(text, (80, 362))

    pygame.display.update()

    flag_1 = True
    flag_2 = True
    while flag_2:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and flag_1:
                pos = pygame.mouse.get_pos()
                if 440 >= pos[0] >= 60 and 190 >= pos[1] >= 60:
                    solve_sudoku_with_animation(grid)
                    flag_1 = False
                elif 440 >= pos[0] >= 60 and 440 >= pos[1] >= 310:
                    solve_sudoku_without_animation(grid)
                    screen.fill((247, 255, 163))
                    draw()
                    pygame.display.update()
                    flag_1 = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and not flag_1:
                    flag_2 = False



if __name__ == "__main__":
    run()