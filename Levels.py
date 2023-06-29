import pygame
import Platform
import Player
from Enemy import Enemy
import multiprocessing as mp
import time

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

        # Enemy update time. Reduce updater interval for faster enemies
        self.last_update_time = time.time()
        self.update_interval = 40
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.all_sprite_list.update()
        self.enemy_sprite_list.update()

        self.player.collider.check_platform_collision(self.player, self.platform_list)
        self.player.collider.check_topBottom_screen(self.player, self.SCREEN_HEIGHT)
        self.player.collider.check_leftRight_screen(self.player, self.SCREEN_WIDTH)
        self.player.input.handle_input("GRAVITY", self.player)

        self.update_enemies()
        for enemy in self.enemy_sprite_list:
            enemy.collider.check_platform_collision(enemy, self.platform_list)
            enemy.collider.check_topBottom_screen(enemy, self.SCREEN_HEIGHT)
            enemy.collider.check_leftRight_screen(enemy, self.SCREEN_WIDTH)
            enemy.collider.check_collision_with_player(self.player, self.enemy_sprite_list)

    def update_enemies(self):
        current_time = time.time()
        if current_time - self.last_update_time >= self.update_interval / 1000:  # Convert milliseconds to seconds
            for enemy in self.enemy_sprite_list:
                enemy.behavior.update(enemy)
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
    """ Definition for level 1. """
 
    def __init__(self, player, SCREEN_WIDTH, SCREEN_HEIGHT):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, SCREEN_WIDTH, SCREEN_HEIGHT)
 
        # List of platforms for the Level
        # Array with x, y, width, height
        level = [[800, 480, 200, 20],
                 [0  , 480, 200, 20],
                 [850, 300, 150, 20],
                 [0  , 300, 150, 20],
                 [400, 350, 200, 20],
                 [600, 50 , 200, 20],
                 [200, 50 , 200, 20]
                 ]
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform.Platform(platform[0], platform[1], platform[2], platform[3], self.GREEN)
            self.platform_list.add(block)

        # Add enemies to the level
        enemy0 = Enemy(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        enemy1 = Enemy(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.enemy_sprite_list.add(enemy0)
        self.enemy_sprite_list.add(enemy1)