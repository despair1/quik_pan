import pandas as pd
import init
import numpy as np
def split(df: pd.DataFrame):
    df_timed = df[(df[init.date_column] >= init.start_date)
                  & (df[init.date_column] <= init.end_date)]
    #df_split = np.array_split(df_timed, init.split)
    # for i in df_split:
    #a = [part[init.min_collumn].apply(np.min) for part in df_split]
    #print(a)
    print(df[init.date_column].iloc[[0,-1]])
    #     print(i)