
from tkinter.ttk import Style
import dash
from dash import dcc
from dash import html
import pandas as pd

df = pd.read_csv("time_series.csv")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



if __name__ == '__main__':
    app.run_server(debug=True)