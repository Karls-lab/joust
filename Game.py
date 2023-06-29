"""
Simple Jouse like game 
Created By Karl Poulson
Version: Alpha 0.2 (Enemy collision, gravity, and screen collision)

Inspiration from:
http://programarcadegames.com/
"""
 
import pygame
from Player import Player 
import Levels 
 
if __name__ == "__main__":
    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (50, 50, 255)
    GREEN = (107,142,35)
    
    # Screen dimensions
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 500

    # Initialized Pygame
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption('JOUST')

    # Create the player, x, y width, height
    player = Player(50, 50)

    # Create all the levels
    level_list = []
    level_list.append(Levels.Level_01(player, SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    # Set the Clock
    clock = pygame.time.Clock()
    done = False


    """ Main Game Loop """
    while not done: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                player.input.handle_input(event, player)            
        
        current_level.update()
        current_level.draw(screen)

        pygame.display.flip()
    
        clock.tick(60)
    
    pygame.quit()