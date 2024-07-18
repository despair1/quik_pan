from flask import Flask,render_template
import pandas as pd
import sys

sys.path.insert(1, "testing")

app = Flask(__name__, static_url_path='/static')
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)
from short_report import short_report
from split_df import split_df
from delta_days import delta_days
from mean_diff import mean_diff

df = pd.read_csv('../ОФЗ 26243 [Price]''.txt')

# print(df.dtypes)
# df = new_time(df)
df = split_df(df)
# for i in df:
#     print(i.describe())
# describe(df)
# t = short_data(df)
df = short_report(df)
df = delta_days(df)
df = mean_diff(df)
l = """
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
"""

@app.route("/")
def hello_world():
    # return l + "<p>Hello, World!</p>" + df.to_html(border=3)
    return render_template('2df.html', df1=df, df2=df)