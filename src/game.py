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
from board import Board
from dragger import Dragger


class Game:

    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
    
    ## show methods

    # show background
    def show_bg(
            self,
            surface
    ):
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

    def show_pieces(
            self,
            surface
    ):
        for row in range(ROWS):
            for col in range(COLS):
                # check if have piece on this square
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    # convert texture into actual image
                    img = pygame.image.load(piece.texture)

                    img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                    piece.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)