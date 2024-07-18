import pandas as pd

from short_report import short_report
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from split_df import split_df

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


# See PyCharm help at https://www.jetbrains.com/help/pycharm/