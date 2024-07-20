import pandas as pd
from short_report import short_report
from split_df import split_df
from delta_days import delta_days
from mean_diff import mean_diff
from extract_ticker import extract_ticker

def first_report(df):
    df = split_df(df)
    df = short_report(df)
    df = delta_days(df)
    df = mean_diff(df)
    ticker = extract_ticker(df)
    return df, ticker
