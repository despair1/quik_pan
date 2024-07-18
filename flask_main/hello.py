from flask import Flask,render_template
import pandas as pd
import sys

sys.path.insert(1, "testing")

app = Flask(__name__, static_url_path='/static')

l = """
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
"""
from file_list import file_list
from first_report import first_report

@app.route("/")
def hello_world():
    # return l + "<p>Hello, World!</p>" + df.to_html(border=3)
    df_all, filenames, str_select = file_list()
    print(str_select)
    df1 = first_report(df_all[0])
    df2 = first_report(df_all[1])
    return render_template('2df.html', df1=df1, df2=df2,
                           str_select=str_select)
