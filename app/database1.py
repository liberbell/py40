import assets.models
import pandas as pd
from assets.database import db_session

df = pd.read_csv("assets/data.csv")
print(df.head())