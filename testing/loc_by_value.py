import pandas as pd
import init


def loc_by_value(df : pd.DataFrame):
    # print(df)
    print(df[(df["<DATE>"] >= init.start_date) & (df["<DATE>"] <= init.end_date)])
    print(df.dtypes)