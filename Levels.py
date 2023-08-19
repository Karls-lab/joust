import pygame
import Platform
from Enemy import Enemy
import time
import random

class Level(object):
    """ 
    This is a generic super-class used to define a level.
    Each level will inherit from this class. This class updates
    enemies and players, and defines the spries. 
    """

    def __init__(self, player, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.platform_list = pygame.sprite.Group()
        self.enemy_sprite_list = pygame.sprite.Group()
        self.all_sprite_list = pygame.sprite.Group()
        self.all_sprite_list.add(player)
        self.player = player
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
         
        # Background image
        self.background = None
        self.GREEN = (107,142,35)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        # Set Gravity
        self.gravity = 0.03

        # Current lives of player
        self.font = pygame.font.Font(None, 36)

        # Enemy update time. Reduce updater interval for faster enemies
        self.last_update_time = time.time()
        self.update_interval = 40


    # Update everythign on this level
    def update(self):
        # Updare the lives counter on the screen
        self.update_scores()

        """ Update everything in this level."""
        self.platform_list.update()
        self.all_sprite_list.update()

        # Update Player and check for collisions
        self.player.collider.check_platform_collision(self.player, self.platform_list)
        self.player.collider.check_topBottom_screen(self.player, self.SCREEN_HEIGHT)
        self.player.collider.check_leftRight_screen(self.player, self.SCREEN_WIDTH)
        self.player.movement.apply_gravity(self.gravity)
        self.player.movement.update(self.player)

        # Update enemies and check for collisions
        self.update_enemies()
        for enemy in self.enemy_sprite_list:
            enemy.collider.check_platform_collision(enemy, self.platform_list)
            enemy.collider.check_topBottom_screen(enemy, self.SCREEN_HEIGHT)
            enemy.collider.check_leftRight_screen(enemy, self.SCREEN_WIDTH)
            enemy.collider.check_collision_with_sprite(self.player, self.enemy_sprite_list)
            enemy.movement.apply_gravity(self.gravity)
            enemy.movement.update(enemy)
            enemy.animation.animate_movement(enemy)


    def update_scores(self):
        text = self.font.render("Lives: " + str(self.player.lives.get_lives()), 1, self.WHITE)
        scoreText = self.font.render("Score: " + str(self.player.score.get_score()), 1, self.WHITE)
        textpos = text.get_rect()
        scoreTextpos = scoreText.get_rect()
        textpos.centerx = self.SCREEN_WIDTH / 4
        textpos.centery = self.SCREEN_HEIGHT + 20
        scoreTextpos.centerx = self.SCREEN_WIDTH / 4
        scoreTextpos.centery = self.SCREEN_HEIGHT + 40  
        screen = pygame.display.get_surface()
        screen.blit(text, textpos)
        screen.blit(scoreText, scoreTextpos)
        pygame.display.update(0, 810, self.SCREEN_WIDTH, 40)


    def update_enemies(self):
        current_time = time.time()
        if current_time - self.last_update_time >= self.update_interval / 1000:  # Convert milliseconds to seconds
            for enemy in self.enemy_sprite_list:
                enemy.behavior.update(enemy, self.player)
            self.last_update_time = current_time        


    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        screen.fill(self.BLACK)
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.all_sprite_list.draw(screen)
        self.enemy_sprite_list.draw(screen)


    def addEnemy(self, enemy):
        self.all_sprite_list.add(enemy)


    def getEnemyList(self):
        return self.enemy_sprite_list

 
"""
Level 01 of the game. Defines the platorms for the Level
"""
class Level_01(Level):
    def __init__(self, player, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__(player, SCREEN_WIDTH, SCREEN_HEIGHT)
 
        # List of platforms for the Level
        # Array with x, y, width, height
        level = [[800, 480, 200, 20],
                 [0  , 480, 200, 20],
                 [850, 300, 150, 20],
                 [0  , 300, 150, 20],
                 [400, 350, 200, 20],
                 [600, 100, 200, 20],
                 [200, 100, 200, 20],
                 [0  , 750,1000, 20]]
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform.Platform(platform[0], platform[1], platform[2], platform[3], self.GREEN)
            self.platform_list.add(block)

        #Add enemies to the level
        enemy0 = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT/2)
        enemy1 = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT/2)
        self.enemy_sprite_list.add(enemy0)
        self.enemy_sprite_list.add(enemy1)


class Level_Generator(Level):
    def __init__(self, player, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__(player, SCREEN_WIDTH, SCREEN_HEIGHT)

        
    def generate_random_level(self, level_no):
        random_widths = random.sample(range(100, 250, 10), 8)
        # Array to store level platforms [x, y, width, height]
        level = [[800, 480, random_widths[0], 20],
                [0  , 480, random_widths[1], 20], 
                [850, 300, random_widths[2], 20],
                [0  , 300, random_widths[3], 20], 
                [400, 350, random_widths[4], 20],
                [600, 100, random_widths[5], 20],
                [200, 100, random_widths[6], 20],
                [0  , 750, random_widths[7], 20]]
        # Create platorms with level array
        for platform_coords in level:
            platform = Platform.Platform(
                platform_coords[0], 
                platform_coords[1], 
                platform_coords[2], 
                platform_coords[3], 
                self.GREEN)
            self.platform_list.add(platform)

        # Add enemies to the level
        if level_no == 0 : level_no += 1
        num_enemies = ((level_no) * 3) // 2
        for i in range(num_enemies):
            enemy = Enemy(random.randint(0, self.SCREEN_WIDTH), self.SCREEN_HEIGHT/2)
            self.enemy_sprite_list.add(enemy)
        