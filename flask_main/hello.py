from flask import Flask
import pandas as pd

app = Flask(__name__)
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"+ df.to_html()