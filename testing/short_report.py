import pandas as pd

import init


def short_data(df :pd.DataFrame):
    ticker = df[init.ticker_column].iat[0]
    print(ticker)
    return ticker