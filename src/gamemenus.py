# AC 2nd Final Project Platformer Menus

# libraries
import pygame
import sys
import csv

WHITE = (255,255,255)
LIGHT = (170,170,170)
DARK = (100,100,100)
BG = (192,192,192)

# setup pygame
pygame.init()
SCREEN = pygame.display.set_mode((800, 600))

font = pygame.font.SysFont("helvetica", 40)
small_font = pygame.font.SysFont("helvetica", 25)
title_font = pygame.font.SysFont("helvetica", 80)

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

        saves_menu_text = title_font.render("Save Menu", True, WHITE)

        save_one_text = font.render("Save 1", True, WHITE)
        save_two_text = font.render("Save 2", True, WHITE)
        save_three_text = font.render("Save 3", True, WHITE)

        save_one_button = pygame.Rect(75, 150, 240, 75)
        save_two_button = pygame.Rect(75, 250, 240, 75)
        save_three_button = pygame.Rect(75, 350, 240, 75)

        quit_text = small_font.render("Quit", True, WHITE)

        quit_button = pygame.Rect(75, 500, 100, 50)

        pygame.draw.rect(screen, LIGHT if save_one_button.collidepoint(mouse) else DARK,save_one_button, border_radius=10)
        pygame.draw.rect(screen, LIGHT if save_two_button.collidepoint(mouse) else DARK, save_two_button, border_radius=10)
        pygame.draw.rect(screen, LIGHT if save_three_button.collidepoint(mouse) else DARK, save_three_button, border_radius=10)

        pygame.draw.rect(screen, LIGHT if quit_button.collidepoint(mouse) else DARK, quit_button, border_radius=10)

        screen.blit(saves_menu_text, (215, 20))
        screen.blit(save_one_text, (135, 165))
        screen.blit(save_two_text, (135, 265))
        screen.blit(save_three_text, (135, 365))
        screen.blit(quit_text, (100, 510))

        def spawn_delete_button():
            delete_save_button = pygame.Rect(100, 100, 300, 300)
            delete_save_text = font.render("Delete Save", True, WHITE)
            pygame.draw.rect(screen, LIGHT if delete_save_button.collidepoint(mouse) else DARK, delete_save_button, border_radius=10)
            screen.blit(delete_save_text, (300, 300))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if save_one_button.collidepoint(mouse):
                    save_selected = "Save One"
                    print(f"Save 1 Button Clicked\nSave Selected: {save_selected}")
                    
                    spawn_delete_button()
                    
                elif save_two_button.collidepoint(mouse):
                    save_selected = "Save Two"
                    print(f"Save 2 Button Clicked\nSave Selected: {save_selected}")

                elif save_three_button.collidepoint(mouse):
                    save_selected = "Save Three"
                    print(f"Save 3 Button Clicked\nSave Selected: {save_selected}")

                elif quit_button.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()


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