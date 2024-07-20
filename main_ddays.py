import pandas as pd

from short_report import short_report
from split_df import split_df
from delta_days import delta_days
from mean_diff import mean_diff
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
    df = mean_diff(df)
    print(df)



