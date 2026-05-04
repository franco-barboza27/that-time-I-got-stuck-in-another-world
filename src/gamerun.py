import pygame
import random
from player import *
from obstacles import *
pygame.init()

map_one=True
if map_one:
    dash=True
elif not map_one:
    dash=False

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

player = pygame.Rect((250, 250, 50, 50))

bird = pygame.Rect((1000, 1000, 50, 50))

running = True
while running:
    gameloop(player, bird)