import pandas as pd

import init


def mean_diff(df: pd.DataFrame):
    df[init.next_mean_collumn] = df[init.mean_column].shift(-1)
    df[init.next_mean_collumn] = df[init.next_mean_collumn] / df[init.mean_column]
    print(df.dtypes)
    df[init.next_mean_collumn] = df[init.next_mean_collumn] ** (365.0 / df[init.delta_days])
    df[init.next_mean_collumn] = (df[init.next_mean_collumn] - 1) * 100

    print(df)