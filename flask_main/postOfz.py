from flask import request, render_template
from file_list import file_list
from first_report import first_report

def test():
    df_all, filenames, str_select = file_list()
    df1 = first_report(df_all[int(request.form["selectLeft"])])
    df2 = first_report(df_all[int(request.form["selectRight"])])
    return render_template('2df.html', df1=df1, df2=df2,
                           str_select=str_select)
    return 'it works! '+filenames[int(request.form["selectLeft"])]
