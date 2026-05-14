import pygame

WHITE = (255,255,255)
LIGHT = (43,147,72)
DARK = (85,166,48)
BG = (192,192,192)


def floatandround(values):
    # Go through each value
    newlist = []
    for item in values:
        try:
            # attempt to make it int
            newitem = int(round(float(item)))
            newlist.append(newitem)
        except:
            # fail
            try:
                # attempt to str it
                info=str(item)
                newlist.append(info)
            except:
                # fail
                try:
                    # try to bool it up
                    newitem = bool(newitem)
                    newlist.append(newitem)
                except:
                    # fail
                    pass
        # success!
    
    # return it
    return newlist

# create buttons using the button parameters+
def create_button(screen, mouse, font_type, text, left, top, width, height, text_width, text_height):
    button_text = font_type.render(text, True, WHITE)
    button = pygame.Rect(left, top, width, height)
    button_rect = pygame.draw.rect(screen, LIGHT if button.collidepoint(mouse) else DARK, button, border_radius=20)
    screen.blit(button_text, (text_width, text_height))

    return button_rect
