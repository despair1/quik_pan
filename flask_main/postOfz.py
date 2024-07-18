from flask import request
from file_list import file_list

def test():
    df_all, filenames, str_select = file_list()
    return 'it works! '+filenames[int(request.form["selectLeft"])]
