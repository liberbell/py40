
from tkinter.ttk import Style
import dash
from dash import dcc
from dash import html
import numpy as np
import plotly.graph_objs as go

np.random.seed(1)
x1 = np.random.randint(0, 100, 50)
y1 = np.random.randint(0, 100, 50)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



if __name__ == '__main__':
    app.run_server(debug=True)