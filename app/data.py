import pandas as pd


df = pd.read_csv("assets/data.csv")
print(df["date"][0])