import init
from short_data import short_data
import pandas as pd

def short_report(df) -> pd.DataFrame:
    data = {init.ticker_column: [],
            init.date_column: [],
            "mean": [],
            "std_m": [],
            "q25%": [],
            init.low25_column: [],
            init.high75_column: []}
    for i in df:
        t,d,m,s, q, l, h = short_data(i)
        data[init.ticker_column].append(t)
        data[init.date_column].append(d)
        data[init.mean_column].append(m)
        data["std_m"].append(s)
        data["q25%"].append(q)
        data[init.low25_column].append(l)
        data[init.high75_column].append(h)
    df = pd.DataFrame(data)
    pd.options.display.float_format = '{:.3f}'.format
    # print(df)
    return df
