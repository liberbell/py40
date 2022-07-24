from tkinter.ttk import Style
import dash
from dash import dcc
from dash import html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id="input-div", value="initial value", type="text"),
])

if __name__ == '__main__':
    app.run_server(debug=True)
