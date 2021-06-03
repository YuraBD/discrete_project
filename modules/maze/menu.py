"""
"""
from pygame.locals import *
import pygame
from maze import maze_game

pygame.font.init()
font = pygame.font.SysFont('comicsans', 40)

class App:
    """
    Main class for an app.
    """

    windowWidth = 500
    windowHeight = 500

    def __init__(self, resolution_width: int, resolutuon_height: int,
                       standard_size: int):
        """
        Initialize app (window) with width, height, wall_size.
        And set a maze.
        """

        self._resolution_widtt = resolution_width
        self._resolutuon_height = resolutuon_height
        self._standard_size = standard_size
        self._running = True

        self._display_surf = None

    def on_init(self):
        """
        Init a display.
        """
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('MAZE SOLVER MENU')
        self._running = True
 
    def on_event(self, event):
        """
        """
        pass

    def on_loop(self):
        pass

    def on_render(self):
        """
        Render.
        """


        self._display_surf.fill((0,0,0))

        text1 = font.render("Step-by-step", True, [0, 0, 0])
        text1_rect = text1.get_rect()
        text1_rect.center = (self.windowWidth//2, self.windowHeight//2 - 125)
        pygame.draw.rect(self._display_surf, (255, 0, 0), pygame.Rect(100, 50, 300, 150))
        self._display_surf.blit(text1, text1_rect)

        text2 = font.render("Solved maze", True, [0, 0, 0])
        text2_rect = text1.get_rect()
        text2_rect.center = (self.windowWidth//2, self.windowHeight//2 + 125)
        pygame.draw.rect(self._display_surf, (255, 0, 0), pygame.Rect(100, 300, 300, 150))
        self._display_surf.blit(text2, text2_rect)

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
        if self.on_init() == False:
            self._running = False

        while self._running:
            self.on_render()
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            if (keys[K_ESCAPE]):
                self._running = False
                self.on_cleanup()

            for ev in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if ev.type == pygame.MOUSEBUTTONDOWN:

                    if 100 <= mouse[0] <= 400 and 50 <= mouse[1] <= 200:
                        self._running = False
                        self.on_cleanup()
                        maze_game.main('mazefile.txt', self._resolution_widtt,
                                                self._resolutuon_height,
                                                self._standard_size, 0)

                    if 100 <= mouse[0] <= 400 and 300 <= mouse[1] <= 450:
                        self._running = False
                        self.on_cleanup()
                        maze_game.main('mazefile.txt', self._resolution_widtt,
                                                self._resolutuon_height,
                                                self._standard_size, 1)



        self.on_cleanup()


def run(path: str, resolution_width: int, resolutuon_height: int,
                                           standard_size: int):
    """
    """

    theApp = App(resolution_width, resolutuon_height, standard_size)
    theApp.on_execute()


if __name__ == "__main__":
    run('mazefile.txt', 864, 1536, 44)
