import saveload
from gamemenus import *
from gamerun import *

def main():
    current_menu = "saves"

    while True:
        if current_menu == "saves":
            result = display_saves_menu(SCREEN)

            if result == "quit":
                pygame.quit()
                sys.exit()

            elif result == "open_ability_menu":
                current_menu = "abilities"


        # ABILITY MENU
        elif current_menu == "abilities":
            result = display_ability_menu(SCREEN)

            if result == "back_to_saves_menu":
                current_menu = "saves"

            elif result == "open_character_menu":
                current_menu = "characters"

        elif current_menu == "characters":
            result = display_character_menu(SCREEN)

            if result == "back_to_abilities_menu":
                current_menu = "abilities"

            elif result == "start_game":
                loop(map)
                current_menu = "saves"

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()