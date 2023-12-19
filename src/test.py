import pandas as pd
from pathlib import Path

MY_DIR = '/folder/where/txt/files/are/saved'

dfs = []
for fp in Path(MY_DIR).rglob('*.txt'):
    dfs.append(pd.read_csv(fp))

df = pd.concat(dfs)