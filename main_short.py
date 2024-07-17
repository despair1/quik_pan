import pandas as pd

import init
from append_short import ashot
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from testing.split_df import split_df
from testing.describe import describe
from testing.short_report import short_data

df = pd.read_csv('../ОФЗ 26226 [Price]''.txt')

if __name__ == '__main__':
    print(df.dtypes)
    # df = new_time(df)
    df = split_df(df)
    # for i in df:
    #     print(i.describe())
    # describe(df)
    # t = short_data(df)
    ashot(df)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/