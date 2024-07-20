from flask import Flask,render_template, session
import pandas as pd
import sys

sys.path.insert(1, "testing")

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'your_secret_key_here'

from file_list import file_list
from first_report import first_report

@app.route("/")
def hello_world():
    # return l + "<p>Hello, World!</p>" + df.to_html(border=3)
    if "start_day" not in session:
        session["start_day"] = 20231004
    df_all, filenames, str_select = file_list()
    # print(str_select)
    df1, ticker_left = first_report(df_all[0])
    df2, ticker_right = first_report(df_all[1])

    return render_template('2df.html', df1=df1, df2=df2,
                           str_select=str_select, default_start_data=session["start_day"],
                           ticker_right=ticker_right, ticker_left=ticker_left)

import postOfz
app.add_url_rule('/process_form', methods=['GET', 'POST'], view_func=postOfz.test)
import date
app.add_url_rule("/date/<int:date1>", view_func=date.date)