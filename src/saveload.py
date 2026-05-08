import pandas as pd
import pathlib

def load(savepath):
    pd.read_csv(savepath)

def levelload(savepath):
    basepath = pathlib.Path(__file__).resolve().parent
    filepath = basepath.parent / 'docs' / savepath

    listblock = []
    rowamount = len(pd.read_csv(filepath))

    for i in range(1, rowamount):
        block = pd.read_csv(filepath, skiprows=lambda x: i != x, dtype={'col1':int, 'col2':int, 'col3':int, 'col4':int, 'col5':str, 'col6':int})

        listblock.append(block.columns.to_list())
    
    return listblock