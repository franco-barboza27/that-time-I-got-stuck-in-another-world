# AC 2nd Final Project Platformer Menus

# libraries
import pygame
import sys
from helpers import *

# constants
WHITE = (255,255,255)
LIGHT = (43,147,72)
DARK = (85,166,48)
BG = (192,192,192)

# setup pygame
pygame.init()

# screen dimensions
SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1395
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# images
# bg image
bg_image = pygame.image.load("docs/menu_bg.png").convert()
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# dash icon
dash_icon = pygame.image.load("docs\Blocks\Ability Icons\dash_icon.png").convert()
dash_icon = pygame.transform.scale(dash_icon, (350, 350))

# double jump icon
double_jump_icon = pygame.image.load("docs\Blocks\Ability Icons\double_jump_icon.png").convert()
double_jump_icon = pygame.transform.scale(double_jump_icon, (350, 350))

# wall climb icon
wall_climb_icon = pygame.image.load("docs\Blocks\Ability Icons\wall_jump_icon.png").convert()
wall_climb_icon = pygame.transform.scale(wall_climb_icon, (350, 350))

# setup fonts
font = pygame.font.Font("docs/Fonts/LVDCGO__.TTF", 45)
small_font = pygame.font.Font("docs/Fonts/LVDCGO__.TTF", 20)
title_font = pygame.font.Font("docs/Fonts/LVDCGO__.TTF", 115)

# display story menu
def display_story_menu(screen):
    continue_button = None
    show_story_menu = True

    while True:
        mouse = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button and continue_button.collidepoint(mouse):
                    return "open_saves_menu"
                elif quit_button and quit_button.collidepoint(mouse):
                    # event quit but button this time(? I didnt write this code :P)
                    return "quit", None
                
        if show_story_menu:
                # displays all the save menu visuals
                screen.blit(bg_image, (0, 0))
                story_title_text = title_font.render("Story", True, WHITE)
                screen.blit(story_title_text, (875, 100))

                story_text_line_one = font.render("You are a normal teenager who was", True, WHITE)
                story_text_line_two = font.render("living their everyday life until one", True, WHITE)
                story_text_line_three = font.render("day they get transported to a ", True, WHITE)
                story_text_line_four = font.render("fantasy world with various obstacles", True, WHITE)
                story_text_line_five = font.render("and hazards blocking your way from", True, WHITE)
                story_text_line_six = font.render("returning to home.", True, WHITE)
                screen.blit(story_text_line_one, (350, 300))
                screen.blit(story_text_line_two, (375, 375))
                screen.blit(story_text_line_three, (445, 450))
                screen.blit(story_text_line_four, (280, 525))
                screen.blit(story_text_line_five, (330, 600))
                screen.blit(story_text_line_six, (750, 675))

                continue_button = create_button(screen, mouse, small_font, "Continue", 1150, 900, 245, 50, 1167.5, 912.5)

                quit_button = create_button(screen, mouse, small_font, "Quit", 100, 1250, 175, 75, 140, 1275)


        pygame.display.update()
            
        
                
# display saves menu
def display_saves_menu(screen):
    show_delete_save = False
    show_edit_buttons = False
    show_deleting_text = False
    show_playing_save = False
    show_display_saves_menu = True
    # base values for menu

    save_selected = ""
    save_one_button = save_two_button = save_three_button = quit_button = delete_button = play_button = yes_button = no_button = go_back_button = None

    while True:
        mouse = pygame.mouse.get_pos()
        # checks if event
        for event in pygame.event.get():
            # event quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # event 1st button clicked
                if save_one_button and save_one_button.collidepoint(mouse):
                    save_selected = "Save 1"
                    edit_button_location = 450
                    edit_text_location = 485
                    show_edit_buttons = True
                # event 2nd button clicked
                elif save_two_button and save_two_button.collidepoint(mouse):
                    save_selected = "Save 2"
                    edit_button_location = 700
                    edit_text_location = 735

                    show_edit_buttons = True
                # event 3rd button clicked
                elif save_three_button and save_three_button.collidepoint(mouse):
                    save_selected = "Save 3"
                    edit_button_location = 950
                    edit_text_location = 985
                    show_edit_buttons = True

                elif quit_button and quit_button.collidepoint(mouse):
                    # event quit but button this time(? I didnt write this code :P)
                    return "quit", None


                elif delete_button and delete_button.collidepoint(mouse):
                    # DELETE save
                    show_display_saves_menu = False
                    show_delete_save = True

                elif play_button and play_button.collidepoint(mouse):
                    # PLAY save (go to next menu)
                    if save_selected != "":
                        if save_selected == "Save 1":
                            savepath = "saveone.csv"
                        elif save_selected == "Save 2":
                            savepath = "savetwo.csv"
                        elif save_selected == "Save 3":
                            savepath = "savethree.csv"
                        # load save
                        savedata = load(savepath)
                        return "open_ability_menu", savedata

                elif yes_button and yes_button.collidepoint(mouse):
                    # Deletes the save (if they clicked delete, and then yes)
                    save_selected = ""

                    show_delete_save = False
                    show_deleting_text = False
                    show_edit_buttons = False
                    show_display_saves_menu = True

                    save_one_button = save_two_button = save_three_button = None
                    delete_button = None
                    play_button = None

                elif no_button and no_button.collidepoint(mouse):
                    # Checks if no was clicked
                    show_delete_save = False
                    show_display_saves_menu = True

                # checks if they try to go back and goes back
                elif go_back_button and go_back_button.collidepoint(mouse):
                    show_delete_save = False
                    show_deleting_text = False
                    show_display_saves_menu = True

            
        if show_display_saves_menu:
            # displays all the save menu visuals
            screen.blit(bg_image, (0, 0))
            saves_menu_text = title_font.render("Save Menu", True, WHITE)
            screen.blit(saves_menu_text, (600, 120))

            save_one_button = create_button(screen, mouse, font, "Save 1", 145, 400, 700, 200, 345, 470)
            save_two_button = create_button(screen, mouse, font, "Save 2", 145, 650, 700, 200, 345, 720)
            save_three_button = create_button(screen, mouse, font, "Save 3", 145, 900, 700, 200, 345, 970)

            quit_button = create_button(screen, mouse, small_font, "Quit", 100, 1250, 175, 75, 140, 1275)
            # made buttons
        if show_edit_buttons:
            # chamnges buttons from base to better
            play_button = create_button(screen, mouse, small_font, "Play Save", 900, edit_button_location, 240, 100, 910, edit_text_location)
            delete_button = create_button(screen, mouse, small_font, "Delete Save", 1175, edit_button_location, 300, 100, 1185, edit_text_location)

        if show_delete_save:
            # shows the ddelete button and conirmation
            screen.blit(bg_image, (0, 0))
            confirm_text = font.render("Are you sure you want to delete:", True, WHITE)
            save_selected_show = font.render(f"{save_selected}", True, WHITE)
            screen.blit(confirm_text, (400, 60))
            screen.blit(save_selected_show, (1100, 175))
            yes_button = create_button(screen, mouse, font, "Yes", 675, 250, 480, 150, 815, 300)
            no_button = create_button(screen, mouse, font, "No", 1275, 250, 480, 150, 1460, 300)

        if show_deleting_text:
            # after delete show stuff
            deleting_text = font.render("Deleting Save...", True, WHITE)
            screen.blit(deleting_text, (275, 300))
            go_back_button = create_button(screen, mouse, small_font, "Go Back", 305, 380, 175, 50, 345, 390)
        
        if show_playing_save:
            # Shows the playing option and plays after (?)
            screen.blit(bg_image, (0, 0))
            playing_save_text = title_font.render(f"Playing {save_selected}", True, WHITE)
            screen.blit(playing_save_text, (0, 0))


        pygame.display.update()

# display ability menu
def display_ability_menu(screen, savedata):
    show_ability_not_unlocked_yet = False
    show_display_ability_menu = True

    ability_selected = ""

    double_jump_button = dash_button = wall_climb_button = go_back_to_saves_menu_button = go_back_button = None
    # set base vars

    while True:
        # checks for events
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                # checks which button was clicked and if its unlocked or no
                if double_jump_button and double_jump_button.collidepoint(mouse):
                    ability_selected = "Double Jump"

                    if savedata[4] == False:
                        ability_selected_location = 950
                        show_ability_not_unlocked_yet = True
                    elif savedata[4] == True:
                        if ability_selected == "Double Jump":
                            return "open_character_menu", ability_selected

                elif dash_button and dash_button.collidepoint(mouse):
                    ability_selected = "Dash"

                    if savedata[5] == False:
                        ability_selected_location = 1125
                        show_ability_not_unlocked_yet = True
                    elif savedata[5] == True:
                        if ability_selected == "Dash":
                            return "open_character_menu", ability_selected

                elif wall_climb_button and wall_climb_button.collidepoint(mouse):
                    ability_selected = "Wall Climb"

                    if savedata[6] == False:
                        ability_selected_location = 1000
                        show_ability_not_unlocked_yet = True
                    elif savedata[6] == True:
                        if ability_selected == "Wall Climb":
                            return "open_character_menu", ability_selected

                # goes back
                elif go_back_button and go_back_button.collidepoint(mouse):
                    show_ability_not_unlocked_yet = False
                    show_display_ability_menu = True

                elif go_back_to_saves_menu_button and go_back_to_saves_menu_button.collidepoint(mouse):
                    return "back_to_saves_menu", None

        if show_display_ability_menu == True:
            # makes the menu look nice
            screen.blit(bg_image, (0, 0))
            
            saves_menu_text = title_font.render("Abilities Menu", True, WHITE)
            screen.blit(saves_menu_text, (350, 150))

            double_jump_button = create_button(screen, mouse, font, "Double Jump", 145, 500, 700, 525, 185, 550)
            screen.blit(double_jump_icon, (325, 650))
            dash_button = create_button(screen, mouse, font, "Dash", 900, 500, 700, 525, 1130, 550)
            screen.blit(dash_icon, (1075, 650))
            wall_climb_button = create_button(screen, mouse, font, "Wall Climb", 1650, 500, 700, 525, 1775, 550)
            screen.blit(wall_climb_icon, (1825, 650))
            go_back_to_saves_menu_button = create_button(screen, mouse, small_font, "Go Back", 100, 1250, 225, 75, 130, 1275)
        
        # checks if its unlocked or NOT
        if show_ability_not_unlocked_yet == True:
            screen.blit(bg_image, (0, 0))

            confirm_text = font.render("Ability not unlocked yet:", True, WHITE)
            ability_selected_show = font.render(f"{ability_selected}", True, WHITE)
            screen.blit(confirm_text, (600, 100))
            screen.blit(ability_selected_show, (ability_selected_location, 200))

            go_back_button = create_button(screen, mouse, small_font,"Go Back", 1127.5, 400, 225, 75, 1150, 425)

        pygame.display.update()

# display character menu
def display_character_menu(screen, savedata):
    # sets the needed variables
    show_character_not_unlocked_yet = False
    show_play_placeholder = False
    show_display_character_menu = True

    character_selected = ""

    character_one_button = character_two_button = character_three_button = go_back_to_saves_menu_button = go_back_button = None

    while True:
        # checks for events
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if character_one_button and character_one_button.collidepoint(mouse):
                    character_selected = "Character 1"

                    # checks each character and if its unlocked or not
                    if savedata[1] == False:
                        show_character_not_unlocked_yet = True
                    elif savedata[1] == True:
                        return "start_game", character_selected

                elif character_two_button and character_two_button.collidepoint(mouse):
                    character_selected = "Character 2"

                    if savedata[2] == False:
                        show_character_not_unlocked_yet = True
                    elif savedata[2] == True:
                        return "start_game", character_selected
                    
                elif character_three_button and character_three_button.collidepoint(mouse):
                    character_selected = "Character 3"

                    if savedata[3] == False:
                        show_character_not_unlocked_yet = True
                    elif savedata[3] == True:
                        return "start_game", character_selected

                elif go_back_button and go_back_button.collidepoint(mouse):
                    show_character_not_unlocked_yet = False
                    show_play_placeholder = False
                    show_display_character_menu = True

                elif go_back_to_saves_menu_button and go_back_to_saves_menu_button.collidepoint(mouse):
                    return "back_to_abilities_menu", None

        if show_display_character_menu == True:
            # makes THIS menu look goo
            screen.blit(bg_image, (0, 0))
            
            character_menu_text = title_font.render("Character Menu", True, WHITE)
            screen.blit(character_menu_text, (200, 160))

            character_one_button = create_button(screen, mouse, font,"Character 1", 145, 500, 700, 200, 180, 550)
            character_two_button = create_button(screen, mouse, font, "Character 2", 900, 500, 700, 200, 925, 550)
            character_three_button = create_button(screen, mouse, font, "Character 3", 1650, 500, 700, 200, 1675, 550)
            go_back_to_saves_menu_button = create_button(screen, mouse, small_font, "Go Back", 100, 1250, 225, 75, 130, 1275)

        if show_character_not_unlocked_yet == True:
            # occurs when char not unlocked
            screen.blit(bg_image, (0, 0))

            confirm_text = font.render("Character not unlocked yet:", True, WHITE)
            character_selected_show = font.render(f"{character_selected}", True, WHITE)
            screen.blit(confirm_text, (450, 100))
            screen.blit(character_selected_show, (900, 200))

            go_back_button = create_button(screen, mouse, small_font,"Go Back", 1127.5, 400, 200, 75, 1140, 425)

        if show_play_placeholder == True:
            # Placeholder for when the menu is closed.
            screen.blit(bg_image, (0, 0))

            playing_text = title_font.render(f"Selected {character_selected}", True, WHITE)
            screen.blit(playing_text, (0, 0))

        # updates the screen.
        pygame.display.update()