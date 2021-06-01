'''A Backtracking program
in Python to solve Sudoku problem'''
 

def find_empty_location(grid, l):
    '''Find entry in the grid that is not used
    Return False if there are no possible entries'''
    for row in range(9):
        for col in range(9):
            if(grid[row][col]== 0):
                l[0]= row
                l[1]= col
                return True
    return False


def used_in_row(grid, row, num):
    '''Check if given number was used in current row'''
    for i in range(9):
        if(grid[row][i] == num):
            return True
    return False


def used_in_col(grid, col, num):
    '''Check if given number was used in current column'''
    for i in range(9):
        if(grid[i][col] == num):
            return True
    return False


def used_in_box(grid, row, col, num):
    '''Check if given number was used in current 3x3 box'''
    for i in range(3):
        for j in range(3):
            if(grid[i + row][j + col] == num):
                return True
    return False


def check_location_is_safe(grid, row, col, num):
    '''Check if it is possible to assign number to given position'''
    return not used_in_row(grid, row, num) and\
           not used_in_col(grid, col, num) and\
           not used_in_box(grid, row - row % 3,
                           col - col % 3, num)
