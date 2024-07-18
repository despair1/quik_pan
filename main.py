import pandas as pd
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from split_df import split_df
from describe import describe
df = pd.read_csv('../ОФЗ 26243 [Price]''.txt')

#print(df)
#print(df.loc[[0,3]])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # get_mins(df, "<LOW>", 1,15,300)
    # loc_by_value(df)
    print(df.dtypes)
    # df = new_time(df)
    df = split_df(df)
    # for i in df:
    #     print(i.describe())
    describe(df)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
