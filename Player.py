from custom_Sprite import custom_Sprite
import pygame

""" Player Class that inherits from custom_Sprite """
class Player(custom_Sprite):
    """Manages player animation, and other essential components need for the player"""
    def __init__(self, x, y):
 
        super().__init__(x, y)
        self.input = InputComponent()
        self.lives = LifeComponent()
        self.score = ScoreComponent()
        self.image = pygame.image.load("assets/player_assets/player_flying_right.png")

    """Player animate functions, update the self.image"""
    def animate_right(self):
        self.image = pygame.image.load("assets/player_assets/player_flying_right.png")

    def animate_left(self):
        self.image = pygame.image.load("assets/player_assets/player_flying_left.png")

    def animate_flap_right(self):
        self.image = pygame.image.load("assets/player_assets/player_flying_flap_right.png")

    def animate_flap_left(self):
        self.image = pygame.image.load("assets/player_assets/player_flying_flap_left.png")


class InputComponent:
    """Handles player input and animation orientation"""
    def __init__(self):
        self.last_input_time = 0
        self.orientation = 'right'
        self.flap = 1


    def handle_input(self, key, player):
        """handles the player input a(left), d(right), and space(jump)"""
        if key[pygame.K_a]:
            player.movement.update_velocity(player, -1, 0)
            player.animate_left()
            self.orientation = 'left'
        elif key[pygame.K_d]:
            player.movement.update_velocity(player, 1, 0)
            player.animate_right()
            self.orientation = 'right'
        elif key[pygame.K_SPACE]:
            player.movement.update_velocity(player, 0, -1)
            self.flap += 1
            if (self.flap % 2 == 0) and self.orientation == 'left':
                player.animate_left()
            elif (self.flap % 2 == 0) and self.orientation == 'right':
                player.animate_right()
            elif self.orientation == 'left':
                player.animate_flap_left()
            elif self.orientation == 'right':
                player.animate_flap_right()


class ScoreComponent:
    def __init__(self):
        self.score = 0
        self.enemies_killed = 0

    def add_enemy_killed(self):
        self.enemies_killed += 1

    def add_score(self):
        self.score += 100 + ((self.enemies_killed + 1) // 10)

    def get_score(self):
        return self.score


class LifeComponent:
    """Handles the lives of the Player"""
    def __init__(self):
        self.lives = 3

    def lose_life(self):
        self.lives -= 1

    def get_lives(self):
        return self.lives
    
    def add_life(self):
        self.lives += 1

    def teleport_to_center(self, player):
        player.movement.set_x(player, 500)
        player.movement.set_y(player, 250)


class AnimationComponent:
    def __init__(self):
        super().__init__()

    def go_right(self):
        print('going right')
        image = pygame.image.load("assets/player_assets/player_flying_right.png")

    def go_left(self):
        print('going left')
        image = pygame.image.load("assets/player_assets/player_flying_left.png")
