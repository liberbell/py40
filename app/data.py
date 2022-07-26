import pandas as pd
import datetime

df = pd.read_csv("assets/data.csv")
# print(type(df["date"][0]))

dates = []
# print(datetime.datetime.strptime(df["date"][0], "%Y/%m/%d").date())
for _date in df["date"]:
    date = datetime.datetime.strptime(_date, "%Y/%m/%d").date()
    dates.append(date)

n_subscribers = df["subscribers"].values
n_reviews = df["reviews"].values