import pandas as pd
import pathlib

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