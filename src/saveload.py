import pandas as pd
import pathlib

def load(savepath):
    pd.read_csv(savepath)

def levelload(savepath):
    basepath = pathlib.Path(__file__).resolve().parent
    filepath = basepath.parent / 'docs' / savepath

    listblock = []
    rowamount = len(pd.read_csv(filepath))

    for i in range(rowamount):
        block = pd.read_csv(filepath, skiprows=lambda x: i != x)

        listblock.append([block])


    
    for block in listblock:
        print(block)

    

levelload('levelone.csv')