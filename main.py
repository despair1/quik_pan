# This is a sample Python script.
import pandas as pd
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from aggregate_periods import get_mins
from testing.loc_by_value import loc_by_value
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
df = pd.read_csv('1''.txt')

#print(df)
#print(df.loc[[0,3]])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # get_mins(df, "<LOW>", 1,15,300)
    loc_by_value(df)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
