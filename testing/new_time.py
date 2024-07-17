import pandas as pd
import init
import numpy as np
def new_time(df: pd.DataFrame) -> (pd.DataFrame, int, int)  :
    #df_split = np.array_split(df_timed, init.split)
    # for i in df_split:
    #a = [part[init.min_collumn].apply(np.min) for part in df_split]
    #print(a)
    start, end = df[init.date_column].iloc[[0, -1]]
    start = max(start, init.start_date)
    end = min(end, init.end_date)
    # print(start, end)
    df_timed = df[(df[init.date_column] >= start)
                  & (df[init.date_column] <= end)]
    # print(df_timed)
    #     print(i)
    return(df_timed, start, end)