# import lib
import pygame
import sys

# custom
from settings import (
    WIDTH,
    HEIGHT,
    COLS,
    ROWS,
    SQSIZE
)
from game import Game

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self):
        while 1:
            self.game.show_bg(surface=self.screen)

            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            

            #update screen
            pygame.display.update()

main = Main() #create instance of Main class
main.mainloop()