# AC 2nd Final Project Platformer Menus

# libraries
import pygame
import sys
import time
import csv

# constants
WHITE = (255,255,255)
LIGHT = (43,147,72)
DARK = (85,166,48)
BG = (192,192,192)

# abilities
double_jump = True
dash = False
wall_climb = False

# save
save_selected = ""


# setup pygame
pygame.init()
SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1395
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg_image = pygame.image.load("docs/menu_bg_placeholder.png").convert()
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("helvetica", 80)
slighty_smaller_font = pygame.font.SysFont("helvetica", 35)
smaller_font = pygame.font.SysFont("helvetica", 20)
small_font = pygame.font.SysFont("helvetica", 40)
title_font = pygame.font.SysFont("helvetica", 160)


# helper functions
# create button
def create_button(screen, mouse, font_type, text, left, top, width, height, text_width, text_height):
    button_text = font_type.render(text, True, WHITE)
    button = pygame.Rect(left, top, width, height)
    button_rect = pygame.draw.rect(screen, LIGHT if button.collidepoint(mouse) else DARK, button, border_radius=10)
    screen.blit(button_text, (text_width, text_height))

    return button_rect


# display saves menu
def display_saves_menu(screen):
    show_delete_save = False
    show_edit_buttons = False
    show_deleting_text = False
    show_playing_save = False
    show_display_saves_menu = True


    save_one_button = save_two_button = save_three_button = quit_button = delete_button = play_button = yes_button = no_button = go_back_button = None

    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if save_one_button and save_one_button.collidepoint(mouse):
                    save_selected = "Save 1"
                    edit_button_location = 450
                    edit_text_location = 475
                    print(f"Save 1 Button Clicked\nSave Selected: {save_selected}")
                    show_edit_buttons = True

                elif save_two_button and save_two_button.collidepoint(mouse):
                    save_selected = "Save 2"
                    edit_button_location = 700
                    edit_text_location = 725
                    print(f"Save 2 Button Clicked\nSave Selected: {save_selected}")
                    show_edit_buttons = True

                elif save_three_button and save_three_button.collidepoint(mouse):
                    save_selected = "Save 3"
                    edit_button_location = 950
                    edit_text_location = 975
                    print(f"Save 3 Button Clicked\nSave Selected: {save_selected}")
                    show_edit_buttons = True

                elif quit_button and quit_button.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()

                elif delete_button and delete_button.collidepoint(mouse):
                    print(f"Deleting {save_selected}")
                    show_display_saves_menu = False
                    show_delete_save = True

                elif play_button and play_button.collidepoint(mouse):
                    if save_selected != "":
                        print(f"Playing {save_selected}")
                        return "open_ability_menu"

                elif yes_button and yes_button.collidepoint(mouse):
                    print(f"Delete {save_selected} here")

                    save_selected = ""

                    show_delete_save = False
                    show_deleting_text = False
                    show_edit_buttons = False
                    show_display_saves_menu = True

                    save_one_button = save_two_button = save_three_button = None
                    delete_button = None
                    play_button = None

                elif no_button and no_button.collidepoint(mouse):
                    show_delete_save = False
                    show_display_saves_menu = True

                elif go_back_button and go_back_button.collidepoint(mouse):
                    show_delete_save = False
                    show_deleting_text = False
                    show_display_saves_menu = True

            
        if show_display_saves_menu:
            screen.blit(bg_image, (0, 0))
            saves_menu_text = title_font.render("Save Menu", True, WHITE)
            screen.blit(saves_menu_text, (925, 100))

            save_one_button = create_button(screen, mouse, font, "Save 1", 145, 400, 700, 200, 367.5, 450)
            save_two_button = create_button(screen, mouse, font, "Save 2", 145, 650, 700, 200, 367.5, 700)
            save_three_button = create_button(screen, mouse, font, "Save 3", 145, 900, 700, 200, 367.5, 950)

            quit_button = create_button(screen, mouse, small_font, "Quit", 100, 1250, 175, 75, 148, 1265)

        if show_edit_buttons:
            play_button = create_button(screen, mouse, small_font, "Play Save", 900, edit_button_location, 240, 100, 930, edit_text_location)
            delete_button = create_button(screen, mouse, small_font, "Delete Save", 1175, edit_button_location, 240, 100, 1185, edit_text_location)

        if show_delete_save:
            screen.blit(bg_image, (0, 0))
            confirm_text = font.render("Are you sure you want to delete:", True, WHITE)
            save_selected_show = font.render(f"{save_selected}", True, WHITE)
            screen.blit(confirm_text, (650, 60))
            screen.blit(save_selected_show, (1100, 175))
            yes_button = create_button(screen, mouse, font, "Yes", 675, 350, 480, 150, 850, 375)
            no_button = create_button(screen, mouse, font, "No", 1275, 350, 480, 150, 1460, 375)

        if show_deleting_text:
            deleting_text = font.render("Deleting Save...", True, WHITE)
            screen.blit(deleting_text, (275, 300))
            go_back_button = create_button(screen, mouse, small_font, "Go Back", 305, 380, 175, 50, 345, 390)
        
        if show_playing_save:
            screen.blit(bg_image, (0, 0))
            playing_save_text = title_font.render(f"Playing {save_selected}", True, WHITE)
            screen.blit(playing_save_text, (0, 0))


        pygame.display.update()

#display_saves_menu(SCREEN)


# display ability menu
def display_ability_menu(screen):
    show_ability_not_unlocked_yet = False
    show_skin_placeholder = False
    show_display_ability_menu = True

    ability_selected = ""

    double_jump_button = dash_button = wall_climb_button = go_back_to_saves_menu_button = go_back_button = None

    while True:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if double_jump_button and double_jump_button.collidepoint(mouse):
                    ability_selected = "Double Jump"
                    print(f"Double Jump Button Clicked\nAbility Selected: {ability_selected}")

                    if double_jump == False:
                        show_ability_not_unlocked_yet = True
                    elif double_jump == True:
                        print("Go to Skin Menu Here")
                        show_skin_placeholder = True

                elif dash_button and dash_button.collidepoint(mouse):
                    ability_selected = "Dash"
                    print(f"Dash Button Clicked\nAbility Selected: {ability_selected}")

                    if dash == False:
                        show_ability_not_unlocked_yet = True
                    elif dash == True:
                        print("Go to Skin Menu Here")
                        show_skin_placeholder = True

                elif wall_climb_button and wall_climb_button.collidepoint(mouse):
                    ability_selected = "Wall Climb"
                    print(f"Wall Climb Button Clicked\nAbility Selected: {ability_selected}")

                    if wall_climb == False:
                        show_ability_not_unlocked_yet = True
                    elif wall_climb == True:
                        print("Go to Skin Menu Here")
                        show_skin_placeholder = True

                elif go_back_button and go_back_button.collidepoint(mouse):
                    show_ability_not_unlocked_yet = False
                    show_skin_placeholder = False
                    show_display_ability_menu = True

                elif go_back_to_saves_menu_button and go_back_to_saves_menu_button.collidepoint(mouse):
                    return "back_to_saves_menu"

        if show_display_ability_menu == True:
            screen.blit(bg_image, (0, 0))
            
            saves_menu_text = title_font.render("Abilities Menu", True, WHITE)
            screen.blit(saves_menu_text, (800, 100))

            double_jump_button = create_button(screen, mouse, font,"Double Jump", 145, 500, 700, 200, 250, 550)
            dash_button = create_button(screen, mouse, font, "Dash", 900, 500, 700, 200, 1130, 550)
            wall_climb_button = create_button(screen, mouse, font, "Wall Climb", 1650, 500, 700, 200, 1800, 550)
            go_back_to_saves_menu_button = create_button(screen, mouse, small_font, "Go Back", 100, 1250, 200, 75, 130, 1265)

        if show_ability_not_unlocked_yet == True:
            screen.blit(bg_image, (0, 0))

            confirm_text = font.render("Ability not unlocked yet:", True, WHITE)
            ability_selected_show = font.render(f"{ability_selected}", True, WHITE)
            screen.blit(confirm_text, (800, 100))
            screen.blit(ability_selected_show, (1125, 200))

            go_back_button = create_button(screen, mouse, small_font,"Go Back", 1127.5, 400, 175, 75, 1140, 410)

        if show_skin_placeholder == True:
            screen.blit(bg_image, (0, 0))

            playing_text = title_font.render(f"Selected {ability_selected}", True, WHITE)
            screen.blit(playing_text, (0, 0))

        pygame.display.update()


#display_ability_menu(SCREEN)

def main():
    while True:
        result = display_saves_menu(SCREEN)

        if result == "quit":
            break

        if result == "open_ability_menu":
            back = display_ability_menu(SCREEN)

            if back == "back_to_saves_menu":
                continue

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()