import pygame

pygame.init()

class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 300, 40, 80)
        self.vel_y = 0
        self.on_ground = False