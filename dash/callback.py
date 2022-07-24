from tkinter.ttk import Style
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id="input-div", value="initial value", type="text"),
    html.Div(id="output-div"),
])

if __name__ == '__main__':
    app.run_server(debug=True)
