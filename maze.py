"""Implemention of the Maze ADT using a 2-D array."""

import pygame
from arrays import Array2D
from lliststack import Stack


class Maze:
    """Define constants to represent contents of the maze cells."""
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

    def __init__(self, num_rows: int, num_cols: int):
        """Creates a maze object with all cells marked as open."""
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._maze_cells = Array2D(num_rows, num_cols)
        self._start_cell = None
        self._curr_cell = None
        self._exit_cell = None
        self._maze_path = Stack()

    def draw(self, display_surf :pygame.Surface, wall_size: int):
        """
        Draw a maze on a display_surf. (wall size is a size of
        blocks on display_surf)
        """

        for row in range(self._num_rows):
            for col in range(self._num_cols):
                if self._maze_cells[row, col] == self.MAZE_WALL:
                    pygame.draw.rect(display_surf, (0, 0, 255),
                                     pygame.Rect(col*wall_size,
                                                 row*wall_size,
                                                 wall_size,
                                                 wall_size))

                if self._maze_cells[row, col] == self.PATH_TOKEN:
                    pygame.draw.rect(display_surf, (255, 255, 0),
                                     pygame.Rect(col*wall_size,
                                                 row*wall_size,
                                                 wall_size,
                                                 wall_size))

                if self._maze_cells[row, col] == self.TRIED_TOKEN:
                    pygame.draw.rect(display_surf, (0, 255, 0),
                                     pygame.Rect(col*wall_size,
                                                 row*wall_size,
                                                 wall_size,
                                                 wall_size))

        curr_row = self._curr_cell.row
        curr_col = self._curr_cell.col
        pygame.draw.rect(display_surf, (255, 0, 0),
                         pygame.Rect(curr_col*wall_size,
                                     curr_row*wall_size,
                                     wall_size,
                                     wall_size), 3)

    def num_rows(self) -> int:
        """Returns the number of rows in the maze."""
        return self._maze_cells.num_rows()

    def num_cols(self) -> int:
        """Returns the number of columns in the maze."""
        return self._maze_cells.num_cols()

    def set_wall(self, row: int, col: int):
        """Fills the indicated cell with a "wall" marker."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._maze_cells[row, col] = self.MAZE_WALL

    def set_start(self, row: int, col: int):
        """Sets the starting cell position."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._start_cell = _CellPosition(row, col)

    def set_exit(self, row: int, col: int):
        """Sets the exit cell position."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._exit_cell = _CellPosition(row, col)

    def make_move(self):
        """
        Make the next move in searching for the exit.
        """
        if self._curr_cell is None:
            self._curr_cell = self._start_cell
            curr_row = self._curr_cell.row
            curr_col = self._curr_cell.col
            self._maze_path.push(self._curr_cell)
            self._mark_path(curr_row, curr_col)
            if self._exit_found(curr_row, curr_col):
                return True

        else:
            curr_row = self._curr_cell.row
            curr_col = self._curr_cell.col
            if self._exit_found(curr_row, curr_col):
                return True
            for direction in [ (-1, 0), (0, 1), (1, 0), (0, -1) ]:
                new_row = curr_row + direction[0]
                new_col = curr_col + direction[1]
                if self._valid_move(new_row, new_col):
                    curr_row = new_row
                    curr_col = new_col
                    self._curr_cell = _CellPosition(curr_row, curr_col)
                    self._maze_path.push(self._curr_cell)
                    self._mark_path(curr_row, curr_col)
                    break
            else:
                self._mark_tried(curr_row, curr_col)
                self._maze_path.pop()
                if self._maze_path.is_empty():
                    return False
                previous_cell = self._maze_path.peek()
                self._curr_cell = previous_cell


    def find_path(self) -> bool:
        """
        Attempts to solve the maze by finding a path from the starting cell
        to the exit. Returns True if a path is found and False otherwise.
        """
        maze_path = Stack()
        first_position = self._start_cell
        curr_row = first_position.row
        curr_col = first_position.col
        maze_path.push(_CellPosition(curr_row, curr_col))
        self._mark_path(curr_row, curr_col)


        while not self._exit_found(curr_row, curr_col):

            for direction in [ (-1, 0), (0, 1), (1, 0), (0, -1) ]:
                new_row = curr_row + direction[0]
                new_col = curr_col + direction[1]
                if self._valid_move(new_row, new_col):
                    curr_row = new_row
                    curr_col = new_col
                    maze_path.push(_CellPosition(curr_row, curr_col))
                    self._mark_path(curr_row, curr_col)
                    break

                else:
                    continue

            else:
                self._mark_tried(curr_row, curr_col)
                maze_path.pop()
                if maze_path.is_empty():
                    return False
                previous_cell = maze_path.peek()
                curr_row = previous_cell.row
                curr_col = previous_cell.col

        return True


    def reset(self):
        """Resets the maze by removing all "path" and "tried" tokens."""
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                if self._maze_cells[row, col] in {self.PATH_TOKEN,
                                                  self.TRIED_TOKEN}:
                    self._maze_cells[row, col] = None

    def __str__(self) -> str:
        """Returns a text-based representation of the maze."""
        output = ""
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                cell = self._maze_cells[row, col]
                if not cell:
                    output += '_ '
                elif cell == self.TRIED_TOKEN:
                    output += f'{self.TRIED_TOKEN} '
                elif cell == self.PATH_TOKEN:
                    output += f'{self.PATH_TOKEN} '
                elif cell == self.MAZE_WALL:
                    output += f'{self.MAZE_WALL} '
            output += "\n"
        return output [:-1]

    def _valid_move(self, row: int, col: int) -> bool:
        """Returns True if the given cell position is a valid move."""
        return row >= 0 and row < self.num_rows() \
               and col >= 0 and col < self.num_cols() \
               and self._maze_cells[row, col] is None

    def _exit_found(self, row: int, col: int) -> bool:
        """Helper method to determine if the exit was found."""
        return row == self._exit_cell.row and col == self._exit_cell.col

    def _mark_tried(self, row: int, col: int):
        """Drops a "tried" token at the given cell."""
        self._maze_cells[row, col] = self.TRIED_TOKEN

    def _mark_path(self, row: int, col: int):
        """Drops a "path" token at the given cell."""
        self._maze_cells[row, col] = self.PATH_TOKEN


class _CellPosition:
    """Private storage class for holding a cell position."""
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col


if __name__ == "__main__":
    pass
