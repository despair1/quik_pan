import pandas as pd

def prev_less(idx_array,   df: pd.DataFrame):
    df1 = pd.DataFrame(idx_array, columns=['Value'])
    print(df1['Value'])
    # print(df[df1['Value']])
    print(df)
    # print(df.iloc(df1[:]))
    # print(df1[0,:])
    print(df.iloc[idx_array])
    print(df.loc[df1['Value']])