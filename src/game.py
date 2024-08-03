# import lib
import pygame

# custom
from settings import (
    WIDTH,
    HEIGHT,
    COLS,
    ROWS,
    SQSIZE
)


class Game:

    def __init__(self):
        pass
    
    ## show methods

    # show background
    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row+col) % 2 == 0:
                    color = (234, 235, 200) #green color
                else:
                    color = (119, 154, 88) #dark green color
                
                rect = (
                    col * SQSIZE,
                    row * SQSIZE,
                    SQSIZE, SQSIZE
                )

                pygame.draw.rect(
                    surface,
                    color,
                    rect
                )