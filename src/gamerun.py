import pygame
from obstacles import *
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

player = pygame.Rect((300, 250, 50, 50))

bird = pygame.Rect((1000, 1000, 50, 50))

run = True
while run:
    playermove(player, bird)
    birdmovement(bird, player, screen)

    if player.colliderect(bird):
        player = player.inflate(1, 1)