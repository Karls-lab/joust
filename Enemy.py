from custom_Sprite import custom_Sprite
import random


""" Enemy Class that inherits from custom_Sprite """
class Enemy(custom_Sprite):
    def __init__(self, x, y):
 
        super().__init__(x, y)
        self.behavior = behaviorComponent()


class behaviorComponent:
    def __init__(self):
        self.behavior = self.setRandomBehavior()

    def setRandomBehavior(self):
        choices = ["Rightflyer", "Leftflyer", "Upflyer", "Downflyer"]
        choice = random.choice(choices)
        print(f"Initial behavior: {choice}")
        return choice

    def update(self, enemy, player):
        # do gravity and wind resistance
        move = .5

        random_choice = random.randint(1, 10)
        if random_choice == 1:
            enemy.movement.update_velocity(enemy, move, -.01)
        elif random_choice == 2:
            enemy.movement.update_velocity(enemy, -move, -.01)
        elif random_choice == 3:
            enemy.movement.update_velocity(enemy, 0, -move)
        elif random_choice == 4:
            enemy.movement.update_velocity(enemy, 0, move)
        # Else, if a roll is 5 enemies behavior
        elif random_choice == 5:
            if self.behavior == "Rightflyer":
                enemy.movement.update_velocity(enemy, move, -.01)
            elif self.behavior == "Leftflyer":
                enemy.movement.update_velocity(enemy, -move, -.01)
            elif self.behavior == "Upflyer":
                enemy.movement.update_velocity(enemy, 0, -move)
            elif self.behavior == "Downflyer":
                enemy.movement.update_velocity(enemy, 0, move)
        elif 6 >= random_choice <= 8:
            if enemy.movement.x_velocity > 0:
                enemy.movement.update_velocity(enemy, -move, 0)
            elif enemy.movement.y_velocity > 0:
                enemy.movement.update_velocity(enemy, 0, -move)
        elif random_choice == 9:
            enemy.movement.update_velocity(enemy, 0, 0)
        # Move to player's position
        else:
            if player.rect.x < enemy.rect.x:
                enemy.movement.update_velocity(enemy, -move, 0)
            elif player.rect.x > enemy.rect.x:
                enemy.movement.update_velocity(enemy, move, 0)
            elif player.rect.y < enemy.rect.y:
                enemy.movement.update_velocity(enemy, 0, -move)
            elif player.rect.y > enemy.rect.y:
                enemy.movement.update_velocity(enemy, 0, move)

