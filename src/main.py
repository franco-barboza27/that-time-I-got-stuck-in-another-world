import saveload
from gamemenus import *
from gamerun import *

def main():
    while True:
        result = display_saves_menu(SCREEN)

        if result == "quit":
            pygame.quit()
            sys.exit()
            break

        if result == "open_ability_menu":
            back = display_ability_menu(SCREEN)

            if back == "back_to_saves_menu":
                continue

        if result =="open_character_menu":
            back = display_character_menu(SCREEN)

            if back == "back_to_abilities_menu":
                continue
        
        if result == "play":
            loop(map)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()