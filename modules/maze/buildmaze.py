"""
This module contains function build_maze
used for building maze.
"""

from maze.maze import Maze


def build_maze(filename):
    """Builds a maze based on a text format in the given file."""
    infile = open(filename, "r")

    # Read the size of the maze.
    nrows, ncols = read_value_pair(infile)
    maze = Maze(nrows, ncols)

    # Read the starting and exit positions.
    row, col = read_value_pair(infile)
    maze.set_start(row, col)
    row, col = read_value_pair(infile)
    maze.set_exit(row, col)

    # Read the maze itself.
    for row in range(nrows):
        line = infile.readline()
        for col in range(len(line)):
            if line[col] == "*":
                maze.set_wall(row, col)

    # Close the maze file and return the newly constructed maze.
    infile.close()

    return [maze, (nrows, ncols)]
    #return maze


def read_value_pair(infile):
    """Extracts an integer value pair from the given input file."""
    line = infile.readline()
    val_a, val_b = line.split()
    return int(val_a), int(val_b)

if __name__ == "__main__":
    pass
