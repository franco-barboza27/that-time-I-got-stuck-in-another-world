import pygame
import random
from helpers import *
from saveload import *
from game import *
from obstacles import *
pygame.init()

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
# declare window settings

def loop(map, charsprite, ability):
    player = Player()
    # make a player object and blocks
    blocks = []
    for block in map:
        # give each block good types
        block = floatandround(block)
        # turn it into a object (the class runs with pygame)
        currblock = obstacle([int(block[0]),int(block[1]),int(block[2]),int(block[3])], block[4], block[5], block[6])
        # add the block to blocklist
        blocks.append(currblock)

    running = True
    while running:
        # run the level with blocks and player :)
        gameloop(player,blocks)