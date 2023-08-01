import pygame

class Menu():
    def __init__(self, screen) -> None:
        self.screen = screen
        self.selection = None
        self.WHITE = (255, 255, 255)

    def draw_menu(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 40)
        start_button = font.render("Press (Space) to Start", True, self.WHITE)
        self.screen.blit(start_button, (self.screen.get_width()/2 - start_button.get_width()/2, 
                                        self.screen.get_height()/2 - start_button.get_height()/2))
        
    def draw_game_over(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 40)
        end_text = font.render("Game Over", True, self.WHITE)
        self.screen.blit(end_text, (self.screen.get_width()/2 - end_text.get_width()/2))



        


