import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 2560, 1395
FPS = 60
GRAVITY = 1
JUMP_HEIGHT = -20
PLAYER_SPEED = 6
AUTO_SCROLL_SPEED = 5

PLATFORM_COLOR = (34, 130, 34)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Test")
clock = pygame.time.Clock()

class block:
    def __init__(self, danger, size, spawndist, coords, sprite=None):
        danger = danger
        size = size
        spawndist = spawndist
        coords = coords
    
    def mover(self, x, y):
        self.coords[0] += x
        self.coords[1] += y
    
    def birdmovement(self, player):
        if player.state=="air" and self.danger=="bird":
            if player.coords[0] >= self.coords[0]:
                xdif = True
            else:
                xdif = False
            if player.coords[1] >= self.coords[1]:
                ydif = True
            else:
                ydif = False

            if xdif == True:
                xdir = 1
            else:
                xdir = -1
            
            if ydif == True:
                ydir = 1
            else:
                ydir = -1
            
        self.mover(10*xdir, 10*ydir)


c = pygame.Rect(block("safe", (100,100), 100, [100, 0]))

