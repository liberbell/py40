import assets.models
import pandas as pd
from assets.database import db_session
import datetime

df = pd.read_csv("assets/data.csv")
print(type(df.iloc[0, 0]))

