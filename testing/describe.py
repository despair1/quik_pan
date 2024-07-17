import pandas as pd
import init


def describe(df):
    pd.options.display.float_format = '{:.2f}'.format
    for i in df:
        print(i[[init.date_column, init.open_column,
                 init.close_column, init.low_collumn,
                 init.high_column, init.vol_column]].describe())
