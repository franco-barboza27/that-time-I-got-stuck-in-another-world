import pygame

"""class block:
    def __init__(self, danger, size, spawndist, coords, sprite=None):
        danger = danger
        size = size
        spawndist = spawndist
        coords = coords"""
    
def mover(bird, x, y):
    bird.move_ip(x, y)
    
def birdmovement(bird, player, screen):
    #if player.state=="air" and bird.danger=="bird":

    if player.left >= bird.left:
        xdif = True
    else:
        xdif = False
    if player.top >= bird.top:
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

    mover(bird, xdir, ydir)

    if player.on_ground == True:
        xdir = xdir*-1
        ydir = ydir*-1
    else:
        pass
        


    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (66,228, 87), bird)