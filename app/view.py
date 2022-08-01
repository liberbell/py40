from turtle import title
import pandas as pd
import datetime
import plotly.graph_objs as go
import dash
from dash import dcc
from dash import html

from assets.database import db_session
from assets.models import Data

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


data = db_session.query(Data.date, Data.subscribers, Data.reviews).all()

dates = []
subscribers = []
reviews = []
for datum in data:
    dates.append(datum.date)
    subscribers.append(datum.subscribers)
    reviews.append(datum.reviews)

diff_subscribers = pd.Series(subscribers).diff().values
diff_reviews = pd.Series(subscribers).diff().values

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(children=[
    html.H2(children='Application by Python Web Scraping.'),
    html.Div(children=[
        dcc.Graph(
            id='subscriber_graph',
            figure={
                'data':[
                    go.Scatter(
                        x=dates,
                        y=subscribers,
                        mode='lines+markers',
                        name='Subscribe num',
                        opacity=0.7,
                        yaxis='y1',
                    ),
                    go.Bar(
                        x=dates,
                        y=diff_subscribers,
                        name='Subscriber diff',
                        yaxis='y2',
                    )
                ],
                'layout': go.Layout(
                    title='Subscribers',
                    xaxis=dict(title='date'),
                    yaxis=dict(title='Subscriber num',side='left', showgrid=False, range=[2500, max(subscribers)+100]),
                    yaxis2=dict(title='Subscriber diff', side='right', overlaying='y', showgrid=False, range=[0, max(diff_subscribers[1:])]),
                    margin=dict(l=200, r=200, b=100, t=200)
                )
            }
        )
    ]),
    html.Div(children=[
        dcc.Graph(
            id='reviewe_graph',
            figure={
                'data':[
                    go.Scatter(
                        x=dates,
                        y=reviews,
                        mode='lines+markers',
                        name='Reviewer num',
                        opacity=0.7,
                        yaxis='y1',
                    ),
                    go.Bar(
                        x=dates,
                        y=diff_reviews,
                        name='Reviews diff',
                        yaxis='y2',
                    )
                ],
                'layout': go.Layout(
                    title='Subscribers',
                    xaxis=dict(title='date'),
                    yaxis=dict(title='Review num', side='left', showgrid=False, range=[0, max(reviews)+10]),
                    yaxis2=dict(title='Reviews diff', side='right', overlaying='y', showgrid=False, range=[0, max(diff_reviews[1:])]),
                    margin=dict(l=200, r=200, b=100, t=200),
                )
            }
        )
    ]),
],style={
    'textAlign': 'center',
    'width': '1200px',
    'margin': '0 auto',
})

if __name__ == '__main__':
    app.run_server(debug=True)