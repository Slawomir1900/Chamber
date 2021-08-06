import linecache
from time import time, ctime, sleep
from pathlib import Path
import pandas as pd


class Logger():
    def __init__(self):
        pass

if __name__ == "__main__":

    path=Path('profile.csv').absolute()
    print(path)
    df=pd.read_csv(filepath_or_buffer=path,sep=',')
    print(df.head())
    print(df['rh'])
