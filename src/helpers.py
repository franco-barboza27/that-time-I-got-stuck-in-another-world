import pygame
import pandas as pd
import pathlib

WHITE = (255,255,255)
LIGHT = (43,147,72)
DARK = (85,166,48)
BG = (192,192,192)

def load(savepath):
    basepath = pathlib.Path(__file__).resolve().parent
    filepath = basepath.parent / 'docs' / savepath

    # skips the rows that arent the first(correct one) and then makes the data have specific types
    save = pd.read_csv(filepath, skiprows=lambda x: 0==x, dtype={'col1':int, 'col1':bool, 'col1':bool, 'col1':bool, 'col1':bool, 'col1':bool, 'col1':bool})
    data = []

    count = 0
    # Reads all of the rows, and goes through each individual value then tries to turn it into an integer, then bool, then string
    for i in range(0, len(save.columns.to_list())):
        info = save.columns.to_list()[i].split(".", 1)[0]
        try:
            info = int(info)
            if count > 0:
                try:
                    info = bool(info)
                except:
                    pass
        except:
            try:
                info=str(info)
            except:
                pass
            
        # add the newly data typed info to a list, and return
            # also why does the dtype= not even work :sob:
        data.append(info)
        count += 1
    
    return data
        

def levelload(savepath):
    basepath = pathlib.Path(__file__).resolve().parent
    filepath = basepath.parent / 'docs' / savepath

    listblock = []
    rowamount = len(pd.read_csv(filepath))

    for i in range(1, rowamount):
        block = pd.read_csv(filepath, skiprows=lambda x: i != x, dtype={'col1':int, 'col2':int, 'col3':int, 'col4':int, 'col5':str, 'col6':int})
        # go through each line, and turn it into a list

        # dtype stuff handled in floatandround
        listblock.append(block.columns.to_list())
    
    return listblock

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
