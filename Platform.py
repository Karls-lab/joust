import pygame


class Platform(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height, color):
        """ Constructor for the wall that the player can run into. """
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    
    def updatePosition(self, x):
        self.rect.x -= x