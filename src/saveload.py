import pandas as pd
import pathlib

def load(savepath):
    basepath = pathlib.Path(__file__).resolve().parent
    filepath = basepath.parent / 'docs' / savepath

    # 1, False, False, False, False, True, False
    save = pd.read_csv(filepath, skiprows=lambda x: 0==x, dtype={'col1':int, 'col1':bool, 'col1':bool, 'col1':bool, 'col1':bool, 'col1':bool, 'col1':bool})
    data = []

    for i in range(0, len(save.columns.to_list())):
        info = save.columns.to_list()[i].split(".", 1)[0]
        try:
            info = int(info)
        except:
            
            try:
                info = bool(info)
            except:
                pass
            
        data.append(info)
    
    return data
        

def levelload(savepath):
    basepath = pathlib.Path(__file__).resolve().parent
    filepath = basepath.parent / 'docs' / savepath

    listblock = []
    rowamount = len(pd.read_csv(filepath))

    for i in range(1, rowamount):
        block = pd.read_csv(filepath, skiprows=lambda x: i != x, dtype={'col1':int, 'col2':int, 'col3':int, 'col4':int, 'col5':str, 'col6':int})

        listblock.append(block.columns.to_list())
    
    return listblock