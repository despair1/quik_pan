import pandas as pd
import init


def delta_days(df: pd.DataFrame):
    df[init.d1_column] = pd.to_datetime(df[init.date_column], format='%Y%m%d')
    df[init.next_day] = df[init.d1_column].shift(-1)
    del df[init.date_column]
    df[init.delta_days] = (df[init.next_day]-df[init.d1_column]).dt.days
    print(df)