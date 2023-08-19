"""
Lance Champions
Created By Karl Poulson
Version: Alpha 2.0
"""
 
import pygame
from Player import Player 
import Levels 
from Display import Menu
from Display import HighScore

if __name__ == "__main__":
    # Colors
    BLACK = (0, 0, 0)
    BLUE = (50, 50, 255)
    GREEN = (107,142,35)
    WHITE = (255, 255, 255)
    
    # Screen dimensions
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800
    INFORMATION_BAR_HEIGHT = 100

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT + INFORMATION_BAR_HEIGHT])
    pygame.display.set_caption('LANCE CHAMPIONS')

    # Create the player, x, y
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/4)

    # Create the level generator
    current_level = Levels.Level_Generator(player, SCREEN_WIDTH, SCREEN_HEIGHT)
    current_level_no = 0

    # Set the Clock
    clock = pygame.time.Clock()
    move_interval = 50 # milliseconds
    last_input_time = 0
    done = False

    # Create the menu Class
    menu = Menu(screen)

    # Set the game state to the menu
    game_state = "start_menu"

    """ Main Game Loop """
    while not done: 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        if game_state == "start_menu":
            menu.draw_menu()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                game_state = "game"

        if game_state == "game_over":
            menu.draw_game_over()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                game_state = "high_scores"

        # if game_state == "high_scores":
        #     # Create a singleton here, and refresh every tick?
        #     high_scores = HighScore(screen)
        #     high_scores.draw_high_scores()
        #     if high_scores.is_high_score(player.score.get_score()):
        #         high_scores.input_score(player.score.get_score())   
        #     keys = pygame.key.get_pressed()
        #     if keys[pygame.K_SPACE]:
        #         game_state = "start_menu"

        if game_state == "next_level":
            menu.draw_next_level(current_level_no)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                current_level_no += 1 
                current_level.generate_random_level(current_level_no)
                game_state = "game"
        
        if game_state == "game":
            if pygame.time.get_ticks() - last_input_time > move_interval:
                keys = pygame.key.get_pressed()
                player.input.handle_input(keys, player) 
                last_input_time = pygame.time.get_ticks()

            if player.lives.get_lives() == 0:
                game_state = "game_over"
            if len(current_level.getEnemyList()) == 0:
                game_state = "next_level"

            # Update the level each tick 
            current_level.update()
            current_level.draw(screen)

        pygame.display.update(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        clock.tick(60)

    pygame.quit()