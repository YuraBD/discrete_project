"""
This module contains function build_maze
used for building maze.
"""

from maze.maze import Maze


def build_maze(path):
    """Builds a maze based on a text format in the given file."""

    # Read the size of the maze.
    nrows, ncols = get_rows_cols(path)
    maze = Maze(nrows, ncols)

    # Read the maze itself.

    with open(path, mode='r', encoding='UTF-8') as infile:
        for row in range(nrows):
            line = infile.readline()
            for col in range(len(line)):
                if line[col] == "*":
                    maze.set_wall(row, col)
                elif line[col] == '0':
                    maze.set_start(row, col)
                elif line[col] == '1':
                    maze.set_exit(row, col)

    # Close the maze file.
    infile.close()

    return [maze, (nrows, ncols)]


def get_rows_cols(path: str) -> tuple :
    """
    Return tuple (nrows, ncols)
    """

    with open(path, mode='r', encoding="UTF-8") as maze_file:
        lines = maze_file.readlines()

    return (len(lines), len(lines[0]))


if __name__ == "__main__":
    pass
