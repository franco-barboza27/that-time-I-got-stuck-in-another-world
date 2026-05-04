# AC 2nd Final Project Platformer Menus

# libraries
import pygame
import sys

WHITE = (255,255,255)
LIGHT = (170,170,170)
DARK = (100,100,100)
BG = (192,192,192)

# setup pygame
pygame.init()
SCREEN = pygame.display.set_mode((800, 600))

font = pygame.font.SysFont("Corbel", 40)

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
"""def exit_game():
    pygame.quit()
    sys.exit()"""

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
def display_saves_menu(screen):
 while True:
        screen.fill(BG)
        mouse = pygame.mouse.get_pos()

        save_one_button = pygame.Rect(100, 300, 140, 50)
        save_two_button = pygame.Rect(100, 380, 140, 50)
        save_three_button = pygame.Rect(100, 460, 140, 50)

        pygame.draw.rect(screen, LIGHT if save_one_button.collidepoint(mouse) else DARK, save_one_button)
        pygame.draw.rect(screen, LIGHT if save_two_button.collidepoint(mouse) else DARK, save_two_button)
        pygame.draw.rect(screen, LIGHT if save_three_button.collidepoint(mouse) else DARK, save_three_button)

        save_one_text = font.render("Save 1", True, WHITE)
        save_two_text = font.render("Save 2", True, WHITE)
        save_three_text = font.render("Save 3", True, WHITE)

        screen.blit(save_one_text, (120, 300))
        screen.blit(save_two_text, (120, 380))
        screen.blit(save_three_text, (120, 460))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                """if play_button.collidepoint(mouse):
                    pass

                if quit_button.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()"""

        pygame.display.update()

display_saves_menu(SCREEN)

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