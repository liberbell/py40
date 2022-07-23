
from tkinter.ttk import Style
import dash
from dash import dcc
from dash import html
import pandas as pd

df = pd.read_csv("time_series.csv")
# print(df.head())
# print(df['MSFT'])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(
        id='sample-line',
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)