import pandas as pd

import init


def short_data(df :pd.DataFrame):
    pd.options.display.float_format = '{:.3f}'.format
    ticker = df[init.ticker_column].iat[0]
    start_date = df[init.date_column].iat[0]
    mean_open = df[init.open_column].mean()
    std_open = df[init.open_column].std()
    q25 = df[init.high_column].quantile(0.75) / \
          df[init.low_collumn].quantile(0.25)
    q25 = (q25-1) * 100
    l25 = df[init.low_collumn].quantile(0.25)
    h75 = df[init.high_column].quantile(0.75)
    # print(ticker, start_date, mean_open, std_open)
    return ticker, start_date, mean_open, std_open, q25, l25, h75
