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

    def update(self, enemy):
        # do gravity and wind resistance
        enemy.movement.update(enemy, 0, .02)
        if enemy.movement.x_velocity > 0:
            enemy.movement.x_velocity -= .01


        random_choice = random.randint(1, 5)
        if random_choice == 1:
            enemy.movement.update(enemy, .5, -.01)
        elif random_choice == 2:
            enemy.movement.update(enemy, -.5, -.01)
        elif random_choice == 3:
            enemy.movement.update(enemy, 0, -.5)
        elif random_choice == 4:
            enemy.movement.update(enemy, 0, .5)
        # Else, if a roll is 5 enemies behavior
        else:
            if self.behavior == "Rightflyer":
                enemy.movement.update(enemy, .3, -.01)
            elif self.behavior == "Leftflyer":
                enemy.movement.update(enemy, -.3, -.01)
            elif self.behavior == "Upflyer":
                enemy.movement.update(enemy, 0, -.3)
            elif self.behavior == "Downflyer":
                enemy.movement.update(enemy, 0, .3)

