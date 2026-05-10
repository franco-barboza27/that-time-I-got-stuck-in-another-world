import pandas as pd
import pathlib

def load(savepath):
    basepath = pathlib.Path(__file__).resolve().parent
    filepath = basepath.parent / 'docs' / savepath

    playervalues = []
    # 1, False, False, False, False, True, False
    block = pd.read_csv(filepath, skiprows=lambda x: 0==x, dtype={'col1':int, 'col1':bool, 'col1':bool, 'col1':bool, 'col1':bool, 'col1':bool, 'col1':bool})
    print(block)

def levelload(savepath):
    basepath = pathlib.Path(__file__).resolve().parent
    filepath = basepath.parent / 'docs' / savepath

    listblock = []
    rowamount = len(pd.read_csv(filepath))

    for i in range(1, rowamount):
        block = pd.read_csv(filepath, skiprows=lambda x: i != x, dtype={'col1':int, 'col2':int, 'col3':int, 'col4':int, 'col5':str, 'col6':int})

        listblock.append(block.columns.to_list())
    
    return listblock

load("docs/saveone.csv")