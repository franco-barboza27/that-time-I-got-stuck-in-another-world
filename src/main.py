from helpers import *
from gamemenus import *
from gamerun import *

def main():
    # Uses strings to determine which menu is being showed
    current_menu = "saves"

    while True:
        if current_menu == "saves":
            # start menu
            result, data = display_saves_menu(SCREEN)

            if result == "quit":
                # checks if quit button pressed
                pygame.quit()
                sys.exit()

            elif result == "open_ability_menu":
                current_menu = "abilities"

        elif current_menu == "abilities":
            # ability menu
            result, ability = display_ability_menu(SCREEN, data)

            if result == "back_to_saves_menu":
                current_menu = "saves"
            # both change the menu to either char/saves
            elif result == "open_character_menu":
                current_menu = "characters"

        elif current_menu == "characters":
            # character menu
            result, charsprite = display_character_menu(SCREEN, data)

            if result == "back_to_abilities_menu":
                current_menu = "abilities"
            # changes menu to either abilit/saves
            elif result == "start_game":
                loop(levelload("levelone.csv"), charsprite, ability)
                current_menu = "saves"

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()