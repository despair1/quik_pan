import pandas as pd
import init


def extract_ticker(df: pd.DataFrame):
    ticker = df[init.ticker_column].iat[0]
    del df[init.ticker_column]
    return ticker
