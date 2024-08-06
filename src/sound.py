# import lib
import pygame

class Sound:

    def __init__(
            self,
            path
    ):
        self.path = path
        # creating pygame sound
        self.sound = pygame.mixer.Sound(path)

    def play(self):
        # play pygame sound
        pygame.mixer.Sound.play(self.sound)