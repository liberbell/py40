import dash
from dash import dcc
from dash import html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout= html.Div([
    html.Label('Dropdown')
])

if __name__ == '__main__':
    app.run_server(debug=True)
