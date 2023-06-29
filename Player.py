from custom_Sprite import custom_Sprite
import pygame

""" Player Class that inherits from custom_Sprite """
class Player(custom_Sprite):
    def __init__(self, x, y):
 
        super().__init__(x, y)
        self.input = InputComponent()

        print("Player created")


class InputComponent:
    def handle_input(self, event, player):
        if event == "GRAVITY":
            player.movement.update(player, 0, .02)
        elif event.key == pygame.K_a:
            player.movement.update(player, -1, 0)
        elif event.key == pygame.K_d:
            player.movement.update(player, 1, 0)
        elif event.key == pygame.K_w:
            player.movement.update(player, 0, -1)
        elif event.key == pygame.K_s:
            player.movement.update(player, 0, 1)