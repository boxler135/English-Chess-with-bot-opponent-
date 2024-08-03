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

        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger

        while 1:
            self.game.show_bg(screen)
            game.show_pieces(screen)

            for event in pygame.event.get():

                # for dragging have 3 events:
                # 1. click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE
                    
                    # if clicked square has a piece
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)

                # 2. target mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_blit(screen)

                # 3. release click
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass

                # quit application
                elif event.type== pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            

            #update screen
            pygame.display.update()

main = Main() #create instance of Main class
main.mainloop()