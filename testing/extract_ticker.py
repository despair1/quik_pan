import pandas as pd
import init


def extract_ticker(df: pd.DataFrame):
    return df[init.ticker_column].iat[0]
