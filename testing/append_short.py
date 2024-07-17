import init
from short_report import short_data
import pandas as pd

def ashot(df):
    data = {init.ticker_column: [],
            init.date_column: [],
            "mean": [],
            "std_m": []}
    for i in df:
        t,d,m,s = short_data(i)
        data[init.ticker_column].append(t)
        data[init.date_column].append(d)
        data["mean"].append(m)
        data["std_m"].append(s)
    df = pd.DataFrame(data)
    pd.options.display.float_format = '{:.3f}'.format
    print(df)
