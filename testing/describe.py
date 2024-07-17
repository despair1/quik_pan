import pandas as pd
import init


def describe(df):
    for i in df:
        print(i.describe())
