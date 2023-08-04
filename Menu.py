import pygame

class Menu():
    def __init__(self, screen) -> None:
        self.screen = screen
        self.selection = None
        self.WHITE = (255, 255, 255)

    
    def draw_text_to_center(self, text, font, color):
        self.screen.fill((0, 0, 0))
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen.get_width()/2, self.screen.get_height()/2)
        self.screen.blit(text_surface, text_rect)


    def draw_menu(self):
        font = pygame.font.SysFont('arial', 40)
        self.draw_text_to_center("Press (Space) to Start", font, self.WHITE)


    def draw_game_over(self):
        font = pygame.font.SysFont('arial', 40)
        self.draw_text_to_center("Game Over", font, self.WHITE)


    def draw_next_level(self, level_no):
        font = pygame.font.SysFont('arial', 40)
        self.draw_text_to_center(f"Level {level_no}", font, self.WHITE)


