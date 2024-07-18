import pandas as pd

import init
from short_report import short_report
from testing.split_df import split_df
from testing.describe import describe
from testing.short_report import short_data
from testing.delta_days import delta_days
from testing.mean_diff import mean_diff
df = pd.read_csv('../ОФЗ 26226 [Price]''.txt')

if __name__ == '__main__':
    print(df.dtypes)
    # df = new_time(df)
    df = split_df(df)
    # for i in df:
    #     print(i.describe())
    # describe(df)
    # t = short_data(df)
    df = short_report(df)
    df = delta_days(df)
    mean_diff(df)



