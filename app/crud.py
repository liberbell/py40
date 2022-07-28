from sqlite3 import Date
from assets.database import db_session
from assets.database import init_db
from assets.models import Data
import datetime

# init_db()
# Create
date = datetime.date.today()
# print(date)
row = Data(date=date, subscribers=3500, reviews=200)
# print(row.reviews)

db_session(row)
db_session.commit()