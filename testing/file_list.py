import os
import pandas as pd
import init


def file_list(start_date: int = 0):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    subdirectory = os.path.join(script_dir, init.ofz_dir)

    txt_files = [f for f in os.listdir(subdirectory) if os.path.isfile(os.path.join(subdirectory, f)) and f.endswith('.txt')]
    s = ""
    for i,filename in enumerate(txt_files):
        s += f'<option value="{i}"> {filename} </option>\n'
    # print(s)
    # print(subdirectory+"\\"+txt_files[0])
    df_all = []
    print(start_date)
    for filename in txt_files:
        df = pd.read_csv(subdirectory+"\\"+filename)
        df_timed = df[(df[init.date_column] >= start_date)]
        df_all.append(df_timed)
    return df_all, txt_files, s
