import pygame

"""class block:
    def __init__(self, danger, size, spawndist, coords, sprite=None):
        danger = danger
        size = size
        spawndist = spawndist
        coords = coords"""
    
class obstacle():
    def __init__(self, rectangle, blocktype, scale, sprite):
        self.rectangle = pygame.Rect(rectangle[0], rectangle[1], rectangle[2], rectangle[3])
        self.sprite = sprite
        self.type = blocktype
        self.scale = scale
    
    def mover(self, x, y):
        self.rectangle.move_ip(x, y)

    def spriteload(self):
        thissprite = pygame.image.load(self.sprite)
        thissprite.transform(thissprite, (self.rectangle[2]*50, self.rectangle[3]*50))
        thissprite.blit(thissprite, (self.rectangle[0], self.rectangle[1]))

    def birdmovement(self, player, screen):
        #if player.state=="air" and bird.danger=="bird":

        if player.left >= self.rectangle.left:
            xdif = True
        else:
            xdif = False
        if player.top >= self.rectangle.top:
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

        self.mover(xdir, ydir)

        if player.on_ground == True:
            xdir = xdir*-1
            ydir = ydir*-1
        else:
            pass