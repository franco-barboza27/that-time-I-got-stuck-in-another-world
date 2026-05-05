import pandas as pd
import pathlib

def load(savepath):
    pd.read_csv(savepath)

def levelload(savepath):
    basepath = pathlib.Path(__file__).resolve().parent
    filepath = basepath.parent / 'docs' / savepath

    blocks = pd.read_csv(filepath)

    

    return blocks