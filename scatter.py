
from tkinter.ttk import Style
import dash
from dash import dcc
from dash import html
import numpy as np
import plotly.graph_objs as go

np.random.seed(1)
x1 = np.random.randint(0, 100, 50)
y1 = np.random.randint(0, 100, 50)

np.random.seed(2)
x2 = np.random.randint(0, 100, 50)
y2 = np.random.randint(0, 100, 50)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(
        id='sample-scatter',
        figure={
            'data':[
                go.Scatter(
                    x=x1,
                    y=y1,
                    mode='markers',
                    opacity=0.2,
                    marker={
                        'size':5
                    },
                    name='Group1',
                ),

                go.Scatter(
                    x=x2,
                    y=y2,
                    mode='markers',
                    opacity=0.5,
                    marker={
                        'size':5
                    },
                    name='Group2',
                )
            ],
            'layout':go.Layout(
                xaxis={'title': "X axis"},
                yaxis={'title': "Y axis"}
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)