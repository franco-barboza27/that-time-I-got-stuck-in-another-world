import pygame

WHITE = (255,255,255)
LIGHT = (43,147,72)
DARK = (85,166,48)
BG = (192,192,192)


def floatandround(values):
    newlist = []
    for item in values:
        try:
            newitem = int(round(float(item)))
            newlist.append(newitem)
        except:
            try:
                info=str(item)
                newlist.append(info)
            except:
                try:
                    newitem = bool(newitem)
                    newlist.append(newitem)
                except:
                    pass

    print(newlist)
    return newlist

# create buttons
def create_button(screen, mouse, font_type, text, left, top, width, height, text_width, text_height):
    button_text = font_type.render(text, True, WHITE)
    button = pygame.Rect(left, top, width, height)
    button_rect = pygame.draw.rect(screen, LIGHT if button.collidepoint(mouse) else DARK, button, border_radius=20)
    screen.blit(button_text, (text_width, text_height))

    return button_rect
