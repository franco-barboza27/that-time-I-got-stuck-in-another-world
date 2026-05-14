import pygame
from obstacles import *
import random

pygame.init()

map_one=True
if map_one:
    dash=True
elif not map_one:
    dash=False
# Declaring the screen/game parameters, NOT GLOBALS BTW
SCREEN_WIDTH, SCREEN_HEIGHT = 2560, 1395
FPS = 60
GRAVITY = 1
JUMP_HEIGHT = -20
PLAYER_SPEED = 6
AUTO_SCROLL_SPEED = 5

SKY_BLUE = (135, 206, 235)
PLAYER_COLOR = (0, 0, 255)
PLATFORM_COLOR = (34, 139, 34)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("That Time I Got Stuck In Another World With No Way Back Home And Had To Use Magical Movement Abilities To Get Warped Back!")
clock = pygame.time.Clock()

class Player:
    def __init__(self):    # x pos, y pos, x width, y height
        self.rect = pygame.Rect(40, 70, 40, 40)
        self.vel_y = 0
        self.on_ground = False
        self.dashing = False
        self.dashTimer = 15
        self.dashClock = 0
        # initializing the player's values 
    
    def move(self, platforms):
        # move function that makes player directions
        dx = 0
        dy = 0
        direction=True
        keys = pygame.key.get_pressed()       
        def respawn():
            self.rect = pygame.Rect(100, 300, 40, 40)
            self.vel_y = 0
            self.on_ground = False
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not self.dashing:
            dx -= PLAYER_SPEED
            direction=False
            
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not self.dashing:
            dx += PLAYER_SPEED
            direction=True
        # changes their direction

        # Dash with cooldown (1 second by default)
        if not hasattr(self, "dash_cooldown"):
            self.dash_cooldown = 0

        # cooldown each frame
        if self.dash_cooldown > 0:
            self.dash_cooldown -= 1

        # Increases speed in the player direction
        if dash==True:
            if keys[pygame.K_SPACE] and self.dash_cooldown == 0:
                dash_amount = 500
                if direction:
                    self.dashing = True
                    self.dashClock = 0
                else:
                    dx -= dash_amount
                # set cooldown in frames (use FPS for ~1 second)
                self.dash_cooldown = FPS

            if self.dashing:
                dx += 34
                self.dashClock += 1

                if self.dashClock >= self.dashTimer:
                    self.dashing = False

        # makes the player go UP!
        if keys[pygame.K_UP] or keys[pygame.K_w] and self.on_ground:
            self.vel_y = JUMP_HEIGHT
            self.on_ground = False


        # quick exits the game
        if keys[pygame.K_DELETE]:
            pygame.quit()
            raise SystemExit

        self.vel_y += GRAVITY
        dy += self.vel_y

        # Collision Handling
        self.on_ground = False
        
        # X Collision
        self.rect.x += dx
        for plat in platforms:
            if self.rect.colliderect(plat.rectangle):
                if dx > 0: self.rect.right = plat.rectangle.left
                if dx < 0: self.rect.left = plat.rectangle.right

        # Y Collision
        self.rect.y += dy
        for plat in platforms:
            if self.rect.colliderect(plat.rectangle):
                if self.vel_y > 0:
                    self.rect.bottom = plat.rectangle.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.rect.top = plat.rectangle.bottom
                    self.vel_y = 0

        # sets the player back to the start if they fall
        if keys[pygame.K_ESCAPE]:
            self.rect = pygame.Rect(100, 300, 40, 40)
            self.vel_y = 0
            self.on_ground = False

        if keys[pygame.K_r]:
            # Reset player state
            respawn()

            # Reset platforms to starting state and return the new list
            platforms = [pygame.Rect(0, 550, 800, 50)]
            platforms += spawn_platforms(400, 10)
    
            # stop further movement processing this frame
            return platforms    

        return platforms
    
    def draw(self):
        pygame.draw.rect(screen, PLAYER_COLOR, self.rect)

def gameloop(player, blocks):
    clock.tick(FPS)

    # Checks if the game was quitted.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    for block in blocks:
        block.rectangle.x -= AUTO_SCROLL_SPEED

    blocks = player.move(blocks)
    # Moves blocks/the player
    blocks = [p for p in blocks if p.rectangle.right > -100]

    screen.fill(SKY_BLUE)
    # updates the blocks and player's position
    for plat in blocks:
        pygame.draw.rect(screen, PLATFORM_COLOR, plat.rectangle)
    player.draw()

    # updates the screen's display
    pygame.display.update()
    return blocks