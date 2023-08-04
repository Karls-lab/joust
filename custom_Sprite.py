import pygame

class custom_Sprite(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
        self.WHITE = (255, 255, 255)
        self.collider = ColliderComponent()
        self.movement = MovementComponent()
 
        # Initialize  dimensions
        self.width = 58
        self.height = 40
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.WHITE)  
  
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height

    def get_x_pos(self):
        return self.rect.x 
    
    def get_y_pos(self):
        return self.rect.y

class ColliderComponent:
    """Prevent the sprite from flying off the screen"""
    def check_topBottom_screen(self, sprite, height):
        if sprite.rect.top < 0:
            sprite.movement.set_y(sprite, 0)
            sprite.movement.stop_y()
        if sprite.rect.bottom > height:
            sprite.movement.set_y(sprite, height - sprite.get_height())
            sprite.movement.stop_y()

    def check_leftRight_screen(self, sprite, width):
        if sprite.get_x_pos() < -sprite.get_width():
            #print("teleporting sprite")
            sprite.movement.set_x(sprite, width)
            print(sprite.get_x_pos())
        if sprite.get_x_pos() > width:
            sprite.movement.set_x(sprite, 0)

    def check_platform_collision(self, sprite, list_of_platforms):
        """Check if sprite collides with any platforms"""
        for platform in list_of_platforms:
            if pygame.sprite.collide_rect(sprite, platform):
                # Top collision
                if sprite.movement.y_velocity > 0 and sprite.rect.bottom -10 <= platform.rect.top:
                    sprite.movement.set_y(sprite, platform.rect.top - sprite.get_height())
                    sprite.movement.stop_y()
                # bottom collision
                elif sprite.movement.y_velocity < 0 and sprite.rect.top + 10 >= platform.rect.bottom:
                    sprite.movement.set_y(sprite, platform.rect.bottom)
                    sprite.movement.stop_y()
                # left collision
                elif sprite.movement.x_velocity > 0 and (sprite.rect.left - sprite.get_width()) < platform.rect.left:
                        sprite.movement.set_x(sprite, platform.rect.left - sprite.get_width())
                        sprite.movement.stop_x()
                # right collision
                elif sprite.movement.x_velocity < 0 and (sprite.rect.right + sprite.get_width()) > platform.rect.right:
                        sprite.movement.set_x(sprite, platform.rect.right)
                        sprite.movement.stop_x()

    """ 
    Check if player collides with any enemies. 
    Returns True if sprite is above enemy, False if sprite is below enemy
    """
    def check_collision_with_sprite(self, player, list_of_sprites):
        for sprite in list_of_sprites:
            if pygame.sprite.collide_rect(player, sprite):
                print("Collision with sprite")
                if player.rect.y < sprite.rect.y:
                    sprite.kill()
                    player.score.add_score()
                    player.score.add_enemy_killed()
                    print("sprite killed")
                elif player.rect.y > sprite.rect.y:
                    if player.lives.get_lives() > 0:
                        player.lives.lose_life()
                        player.lives.teleport_to_center(player)
                        print("player lost life")
                    else:
                        player.kill()
                        print("player killed")


class MovementComponent:
    def __init__(self):
        self.x_velocity = 0
        self.y_velocity = 0
        self.max_velocity = 8

    def update_velocity(self, sprite, x, y):
        self.x_velocity += x
        self.y_velocity += y

        # Limit velocity
        if self.x_velocity > 0:
            self.x_velocity = min(self.x_velocity, self.max_velocity)
        elif self.x_velocity < 0:
            self.x_velocity = max(self.x_velocity, -self.max_velocity)
        elif self.y_velocity > 0:
            self.y_velocity = min(self.y_velocity, self.max_velocity)
        elif self.y_velocity < 0:
            self.y_velocity = max(self.y_velocity, -self.max_velocity)


    def update(self, sprite):
        sprite.rect.x += self.x_velocity
        sprite.rect.y += self.y_velocity

    def set_y(self, sprite, new_y):
        sprite.rect.y = new_y

    def set_x(self, sprite, new_x):
        sprite.rect.x = new_x

    def stop_y(self):
        self.y_velocity = 0

    def stop_x(self):
        self.x_velocity = 0

    def apply_wind_resistance(self, x):
        # if self.x_velocity > 0:
        #     self.x_velocity -= x
        # elif self.x_velocity < 0:
        #     self.x_velocity += x
        pass
   
    def apply_gravity(self, y):
        self.y_velocity += y
