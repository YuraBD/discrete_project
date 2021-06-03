from pygame.locals import *
import pygame
from maze.buildmaze import build_maze
from maze.maze import Maze
import time


class App:
    """
    Main class for an app.
    """

    def __init__(self, maze: Maze, width: int,
                 height: int, wall_size: int, mode: int):
        """
        Initialize app (window) with width, height, wall_size.
        And set a maze.
        """

        self._mode = mode
        self._state = None
        self._running = True
        self._display_surf = None
        self._path_surf = None
        self._block_surf = None
        self.maze = maze
        self.windowWidth = width
        self.windowHeight = height
        self.wall_size = wall_size
 
    def on_init(self):
        """
        Init a display.
        """
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('MAZE SOLVER BACKTRACKING')
        self._running = True

    def on_render(self):
        """
        Render.
        """
        self._display_surf.fill((0,0,0))

        if self._mode == 0:

            self._state = self.maze.make_move()
            pygame.time.wait(1500)

        self.maze.draw(self._display_surf, self.wall_size)


        pygame.display.flip()
 
    def on_cleanup(self):
        """
        Exit the app.
        """
        pygame.quit()

    def on_execute(self):
        """
        Main function.
        """
        self.on_init()

        if self._mode == 1:
            self.maze.find_path()

        while( self._running ) and (self._state is None):
            self.on_render()
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_ESCAPE]):
                self._running = False
                self.on_cleanup()

        if self._state == False:
            print('No path!')
            print(self.maze)
        elif self._state == True:
            print('Path found!')
            print(self.maze)
        while self._running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            if (keys[K_ESCAPE]):
                self._running = False
                self.on_cleanup()


def main(path: str, resolution_width: int, resolutuon_height: int,
                            standard_size: int, mode: int):
    """
    Run a program. Requires resolution parameters (with a scale)
    Standard size - is a size of one block.
    """

    standard_size_a = standard_size_b = standard_size
    maze_params = build_maze(path)
    maze = maze_params[0]
    nrows, ncols = maze_params[1]
    if nrows*standard_size > resolution_width:
        standard_size_a = resolution_width // nrows
    if ncols*standard_size > resolutuon_height:
        standard_size_b = resolutuon_height // ncols

    if standard_size_a <= standard_size_b:
        standard_size = standard_size_a
    else:
        standard_size = standard_size_b

    screen_width = standard_size * ncols
    screen_height = standard_size * nrows

    theApp = App(maze, screen_width, screen_height, standard_size, mode)
    theApp.on_execute()


if __name__ == "__main__" :
    main('mazefile.txt', 864, 1536, 44, 1)
    # main('mazefile1.txt', 864, 1536, 44)
