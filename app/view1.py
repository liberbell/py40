from assets.database import db_session
from assets.models import Data
import pandas as pd

data = db_session.query(Data.date, Data.subscribers, Data.reviews).all()
print(data[0])