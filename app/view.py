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


n_subscribers 