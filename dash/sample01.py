import dash
from dash import dcc
from dash import html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout= html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': "Bob", 'value': "bob"},
            {'label': "Eric", 'value': "eric"},
            {'label': "Alex", 'value': "alex"},
        ],
        value='eric',
    ),
    html.Label('Multi-select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': "Bob", 'value': "bob"},
            {'label': "Eric", 'value': "eric"},
            {'label': "Alex", 'value': "alex"},
        ],
        value=['eric', 'alex'],
        multi=True,
    ),
    html.Label('Radio botton'),
    dcc.RadioItems(
        options=[
            {'label': "Bob", 'value': "bob"},
            {'label': "Eric", 'value': "eric"},
            {'label': "Alex", 'value': "alex"},
        ],
        value='eric',
    ),
    html.Label('Check boxes'),
    dcc.Checklist(
        options=[
            {'label': "Bob", 'value': "bob"},
            {'label': "Eric", 'value': "eric"},
            {'label': "Alex", 'value': "alex"},
        ],
        value=['eric', 'alex']
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
