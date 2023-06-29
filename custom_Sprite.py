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
        self.width = 15
        self.height = 25
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
    """Prevent the player from flying off the screen"""
    def check_topBottom_screen(self, player, height):
        if player.rect.top < 0:
            player.movement.set_y(player, 0)
            player.movement.stop_y()
        if player.rect.bottom > height:
            player.movement.set_y(player, height - player.get_height())
            player.movement.stop_y()

    def check_leftRight_screen(self, player, width):
        if player.get_x_pos() < -player.get_width():
            #print("teleporting player")
            player.movement.set_x(player, width)
            print(player.get_x_pos())
        if player.get_x_pos() > width:
            player.movement.set_x(player, 0)

    def check_platform_collision(self, player, list_of_platforms):
        """Check if player collides with any platforms"""
        for platform in list_of_platforms:
            if pygame.sprite.collide_rect(player, platform):
                """ top collision"""
                if player.movement.y_velocity > 0 and player.rect.bottom -5 <= platform.rect.top:
                    player.movement.set_y(player, platform.rect.top - player.get_height())
                    player.movement.stop_y()
                    #print("top collision")
                elif player.movement.y_velocity < 0 and player.rect.top + 5 >= platform.rect.bottom:
                    player.movement.set_y(player, platform.rect.bottom)
                    player.movement.stop_y()
                    #print("bottom collision")
                else:
                    if player.movement.x_velocity > 0 and (player.rect.left - player.get_width()) < platform.rect.left:
                        player.movement.set_x(player, platform.rect.left - player.get_width())
                        player.movement.stop_x()
                        #print("left collision")
                    elif player.movement.x_velocity < 0 and (player.rect.right + player.get_width()) > platform.rect.right:
                        player.movement.set_x(player, platform.rect.right)
                        player.movement.stop_x()
                        #print("right collision")

    """ Check if player collides with any enemies. 
    Returns True if player is above enemy, False if player is below enemy"""
    def check_collision_with_player(self, player, list_of_sprites):
        for sprite in list_of_sprites:
            if pygame.sprite.collide_rect(player, sprite):
                if player.rect.y < sprite.rect.y:
                    sprite.kill()


class MovementComponent:
    def __init__(self):
        self.x_velocity = 0
        self.y_velocity = 0

    def update(self, player, x, y):
        self.apply_wind_resistance(.01)
        self.x_velocity += x 
        self.y_velocity += y 
        player.rect.x += self.x_velocity
        player.rect.y += self.y_velocity

    def set_y(self, player, new_y):
        player.rect.y = new_y

    def set_x(self, player, new_x):
        player.rect.x = new_x

    def stop_y(self):
        self.y_velocity = 0

    def stop_x(self):
        self.x_velocity = 0

    def apply_wind_resistance(self, x):
        if self.x_velocity > 0:
            self.x_velocity -= x
        elif self.x_velocity < 0:
            self.x_velocity += x