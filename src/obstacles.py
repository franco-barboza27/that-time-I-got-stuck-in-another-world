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

player = pygame.Rect((300, 250, 50, 50))

bird = pygame.Rect((1000, 1000, 50, 50))

class block:
    def __init__(self, danger, size, spawndist, coords, sprite=None):
        danger = danger
        size = size
        spawndist = spawndist
        coords = coords
    
def mover(bird, x, y):
        bird.move_ip(x, y)
    
def birdmovement(bird, player):
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

run = True
while run:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (66,228, 87), bird)

    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True:
        player.move_ip(0, -2)
    
    if key[pygame.K_a] == True:
        player.move_ip(-2, 0)
    
    if key[pygame.K_s] == True:
        player.move_ip(0, 2)
    
    if key[pygame.K_d] == True:
        player.move_ip(2, 0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    birdmovement(bird, player)
    
    pygame.display.update()

pygame.quit()