from custom_Sprite import custom_Sprite
import random
import pygame


""" Enemy Class that inherits from custom_Sprite """
class Enemy(custom_Sprite):
    def __init__(self, x, y):
 
        super().__init__(x, y)
        self.behavior = behaviorComponent()
        self.animation = AnimationComponent()
        self.image = pygame.image.load("assets/enemy_assets/enemy_flying_right.png")

    def animate_right(self):
        self.image = pygame.image.load("assets/enemy_assets/enemy_flying_right.png")
    
    def animate_left(self):
        self.image = pygame.image.load("assets/enemy_assets/enemy_flying_left.png")

    def animate_flap_right(self):
        self.image = pygame.image.load("assets/enemy_assets/enemy_flying_flap_right.png")

    def animate_flap_left(self):
        self.image = pygame.image.load("assets/enemy_assets/enemy_flying_flap_left.png")


class behaviorComponent:


    def update(self, enemy, player):
        # The move variable determiens how fase the enemy moves 
        move = .5

        random_choice = random.randint(1, 12)
        # update velocity (enemy, x, y)
        if random_choice == 1:
            enemy.movement.update_velocity(enemy, x=move, y=0)
        elif random_choice == 2:
            enemy.movement.update_velocity(enemy, x=-move, y=0)
        elif random_choice == 3:
            enemy.movement.update_velocity(enemy, x=0, y=-move)
        elif random_choice == 4:
            enemy.movement.update_velocity(enemy, x=0, y=move)
        elif random_choice == 5:
            enemy.movement.update_velocity(enemy, x=0, y=-move*2)
        elif random_choice == 6:
            enemy.movement.update_velocity(enemy, x=0, y=0)
        # Else, move to player's position
        else:
            if player.rect.x < enemy.rect.x:
                enemy.movement.update_velocity(enemy, x=-move, y=0)
            elif player.rect.x > enemy.rect.x:
                enemy.movement.update_velocity(enemy, x=move, y=0)
            elif player.rect.y < enemy.rect.y:
                enemy.movement.update_velocity(enemy, x=0, y=-move)
            elif player.rect.y > enemy.rect.y:
                enemy.movement.update_velocity(enemy, x=0, y=move)


class AnimationComponent:


    def animate_movement(self, enemy):
        if enemy.movement.x_velocity > 0:
            enemy.animate_right()
        if enemy.movement.x_velocity < 0:
            enemy.animate_left()
        elif enemy.movement.y_velocity > 0:
            enemy.animate_flap_right()
        elif enemy.movement.y_velocity < 0:
            enemy.animate_flap_left()
        else:
            enemy.animate_right()

