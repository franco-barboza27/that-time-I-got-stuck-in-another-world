# AC 2nd Final Project Platformer Menus

# libraries
import pygame
import sys
import csv

# constants
WHITE = (255,255,255)
LIGHT = (170,170,170)
DARK = (100,100,100)
BG = (192,192,192)

#bg_image = pygame.image.load("menu_bg_placeholder.png").convert()
#bg_image = pygame.transform.scale(bg_image, (800,600))

# setup pygame
pygame.init()
SCREEN = pygame.display.set_mode((800, 600))

font = pygame.font.SysFont("helvetica", 40)
small_font = pygame.font.SysFont("helvetica", 25)
title_font = pygame.font.SysFont("helvetica", 80)


# helper functions
# create button
def create_button(screen, mouse, font_type, text, left, top, width, height, text_width, text_height):
    button_text = font_type.render(text, True, WHITE)
    button = pygame.Rect(left, top, width, height)
    button_rect = pygame.draw.rect(screen, LIGHT if button.collidepoint(mouse) else DARK, button, border_radius=10)
    screen.blit(button_text, (text_width, text_height))

    return button_rect

# saves menu:
# delete save
def delete_save(screen, mouse, font):
    def create_delete_button():
        delete_button = create_button(screen, mouse, font, "Delete Save", 150, 150, 240, 75, 135, 165)
        return delete_button
    create_delete_button()

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
        screen.blit(saves_menu_text, (215, 20))

        save_one_button = create_button(screen, mouse, font, "Save 1", 75, 150, 240, 75, 135, 165)
        save_two_button = create_button(screen, mouse, font, "Save 2", 75, 250, 240, 75, 135, 265)
        save_three_button = create_button(screen, mouse, font, "Save 3", 75, 350, 240, 75, 135, 365)

        quit_button = create_button(screen, mouse, small_font, "Quit", 75, 500, 100, 50, 100, 510)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if save_one_button.collidepoint(mouse):
                    save_selected = "Save One"
                    print(f"Save 1 Button Clicked\nSave Selected: {save_selected}")
    
                    delete_button = create_button(screen, mouse, font, "Delete Save", 75, 450, 240, 75, 135, 465)

                    if delete_button.collidepoint(mouse):
                        pass
                    
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
def display_map_menu(screen):
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