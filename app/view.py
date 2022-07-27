import pandas as pd
import datetime
import plotly.graph_objs as go
import dash
from dash import dcc
from dash import html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv("assets/data.csv")
dates = []
for _date in df["date"]:
    date = datetime.datetime.strptime(_date, "%Y/%m/%d").date()
    dates.append(date)

n_subscribers = df["subscribers"].values
n_reviews = df["reviews"].values

diff_subscribers = df["subscribers"].diff().values
diff_reviews = df["reviews"].diff().values
# print(diff_reviews)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H2(children='Application by Python Web Scraping.'),
    html.Div(children=[
        dcc.Graph(
            id='subscriber_graph',
            figure={
                'data':[
                    go.Scatter(
                        x=dates,
                        y=n_subscribers,
                        mode='lines+markers',
                        name='Subscribe num',
                        opacity=0.7,
                        yaxis='y1',
                    ),
                    go.Bar(
                        x=dates,
                        y=diff_subscribers,
                        name='Subscriber diff',
                        opacity=0.7,
                        yaxis='y1',
                    )
                ]
            }
        )
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)