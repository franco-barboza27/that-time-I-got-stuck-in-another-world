# AC 2nd Final Project Platformer Menus

# libraries
import pygame
import sys
import time
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
smaller_font = pygame.font.SysFont("helvetica", 20)
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
    show_delete_save = False
    show_edit_buttons = False
    show_deleting_text = False
    show_playing_save = False
    show_display_saves_menu = True

    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if save_one_button.collidepoint(mouse):
                    save_selected = "Save 1"
                    edit_button_location = 165.5
                    edit_text_location = 177.5
                    print(f"Save 1 Button Clicked\nSave Selected: {save_selected}")
                    show_edit_buttons = True
                    
                elif save_two_button.collidepoint(mouse):
                    save_selected = "Save 2"
                    edit_button_location = 265.5
                    edit_text_location = 277.5
                    print(f"Save 2 Button Clicked\nSave Selected: {save_selected}")
                    show_edit_buttons = True

                elif save_three_button.collidepoint(mouse):
                    save_selected = "Save 3"
                    edit_button_location = 365.5
                    edit_text_location = 377.5
                    print(f"Save 3 Button Clicked\nSave Selected: {save_selected}")
                    show_edit_buttons = True

                elif quit_button.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()

                elif delete_button.collidepoint(mouse):
                    print(f"Deleting {save_selected}")
                    show_display_saves_menu = False
                    show_delete_save = True

                elif play_button.collidepoint(mouse):
                    print(f"Playing {save_selected}")
                    show_playing_save = True

                elif yes_button.collidepoint(mouse):
                    show_deleting_text = True
                    print(f"Delete {save_selected} here")
                    show_display_saves_menu = True

                elif no_button.collidepoint(mouse):
                    show_delete_save = False
                    show_display_saves_menu = True

                elif go_back_button.collidepoint(mouse):
                    show_delete_save = False
                    show_deleting_text = False
                    show_display_saves_menu = True

            
        if show_display_saves_menu == True:
            screen.fill(BG)
            saves_menu_text = title_font.render("Save Menu", True, WHITE)
            screen.blit(saves_menu_text, (215, 20))

            save_one_button = create_button(screen, mouse, font, "Save 1", 75, 150, 240, 75, 135, 165)
            save_two_button = create_button(screen, mouse, font, "Save 2", 75, 250, 240, 75, 135, 265)
            save_three_button = create_button(screen, mouse, font, "Save 3", 75, 350, 240, 75, 135, 365)

            quit_button = create_button(screen, mouse, small_font, "Quit", 75, 500, 100, 50, 100, 510)

        if show_edit_buttons == True:
            play_button = create_button(screen, mouse, smaller_font, "Play Save", 340, edit_button_location, 120, 50, 357.5, edit_text_location)
            delete_button = create_button(screen, mouse, smaller_font, "Delete Save", 475, edit_button_location, 120, 50, 480, edit_text_location)

        if show_delete_save == True:
            screen.fill(BG)
            confirm_text = font.render("Are you sure you want to delete:", True, WHITE)
            save_selected_show = font.render(f"{save_selected}", True, WHITE)
            screen.blit(confirm_text, (100, 30))
            screen.blit(save_selected_show, (350, 80))
            yes_button = create_button(screen, mouse, font, "Yes", 140, 200, 240, 75, 230, 215)
            no_button = create_button(screen, mouse, font, "No", 410, 200, 240, 75, 500, 215)

        if show_deleting_text == True:
            deleting_text = font.render("Deleting Save...", True, WHITE)
            screen.blit(deleting_text, (275, 300))
            go_back_button = create_button(screen, mouse, small_font, "Go Back", 305, 380, 175, 50, 345, 390)
        
        if show_playing_save == True:
            screen.fill(BG)
            playing_save_text = title_font.render(f"Playing {save_selected}")
            screen.blit(playing_save_text, (0, 0))


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