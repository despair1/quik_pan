import pandas as pd


def count_up(idx_array, column_name,  df: pd.DataFrame):
    idx_up = []
    for i, idx in enumerate(idx_array):
        if i > 0:
            prev = idx_array[i-1]
            print(df.loc[prev, column_name], df.loc[idx, column_name])