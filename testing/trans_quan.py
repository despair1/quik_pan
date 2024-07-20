import pandas as pd
import init


def trans_quan(df: pd.DataFrame):
    df[init.high75_column] = df[init.high75_column].shift(-1)
    df[init.trans_quan] = df[init.high75_column]/df[init.low25_column]
    df[init.trans_quan] = (df[init.trans_quan]-1)*100
    del df[init.high75_column]
    del df[init.low25_column]
    return df
