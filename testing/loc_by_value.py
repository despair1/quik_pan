import pandas as pd


def loc_by_value(df : pd.DataFrame):
    # print(df)
    print(df[(df["<DATE>"] >= 20210219) & (df["<DATE>"] <= 20210223)])
    print(df.dtypes)