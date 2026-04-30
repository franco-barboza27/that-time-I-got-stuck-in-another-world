# AC 2nd Final Project Platformer Menus

# libraries
import pygame
import sys

WHITE = (255,255,255)
LIGHT = (170,170,170)
DARK = (100,100,100)
BG = (60,25,60)
font = pygame.font.SysFont("Arial", 40)

# setup pygame
pygame.init()
screen = pygame.display.set_mode(720, 720)
pygame.display.set_caption("PLACEHOLDER")

    

# saves menu:
# delete save
def delete_save():
    # ask user if they are are sure saved as choice
    choice = None
    if choice == "Yes":
        # clear the selected save's CSV data (Franco)
        pass
    if choice == "No":
        # exit func
        pass

# exit game
def exit_game():
    pygame.quit()
    sys.exit()

# load save
def load_save():
    # from (name of save selected) get the saves data (Franco’s Part)
    pass

# editing save
def editing_save():
    pass

# create new save
def create_new_save():
    pass

# display saves menu
def display_saves_menu():
    while True:
        screen.fill(BG)
        mouse = pygame.mouse.get_pos()

        play_button = pygame.Rect(300, 300, 140, 50)
        quit_button = pygame.Rect(300, 380, 140, 50)

        pygame.draw.rect(screen, LIGHT if play_button.collidepoint(mouse) else DARK, play_button)
        pygame.draw.rect(screen, LIGHT if quit_button.collidepoint(mouse) else DARK, quit_button)

        play_text = font.render("Play", True, WHITE)
        quit_text = font.render("Quit", True, WHITE)

        screen.blit(play_text, (335, 305))
        screen.blit(quit_text, (335, 385))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if play_button.collidepoint(mouse):
                    pass

                if quit_button.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

display_saves_menu()

# map menu:
# level select
def level_select():
    pass

# display map menu
def display_map_menu():
    pass


# ability menu:
# ability select
def ability_select():
    pass

# display ability menu
def display_ability_menu():
    pass


# character menu:
# character select
def character_select():
    pass

# display character menu
def display_character_menu():
    pass