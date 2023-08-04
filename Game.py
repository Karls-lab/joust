"""
Lance Champions
Created By Karl Poulson
Version: Alpha 2.0
"""
 
import pygame
from Player import Player 
import Levels 
from Menu import Menu

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

    # Initialized Pygame
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT + INFORMATION_BAR_HEIGHT])
    pygame.display.set_caption('LANCE CHAMPIONS')

    # Create the player, x, y
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/4)

    # Create all the levels
    level_list = []
    level_list.append(Levels.Level_01(player, SCREEN_WIDTH, SCREEN_HEIGHT))
    level_list.append(Levels.Level_02(player, SCREEN_WIDTH, SCREEN_HEIGHT))
    level_list.append(Levels.Level_03(player, SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

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
            if keys[pygame.K_SPACE]:
                game_state = "game"

        if game_state == "game_over":
            menu.draw_game_over()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                done = True

        if game_state == "next_level":
            menu.draw_next_level(current_level_no + 2)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                current_level_no += 1
                current_level = level_list[current_level_no]
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


            current_level.update()
            current_level.draw(screen)

        pygame.display.update(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        clock.tick(60)

    pygame.quit()