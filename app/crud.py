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

# db_session.add(row)
# db_session.commit()

row1 = Data(date=date, subscribers=6500, reviews=210)
row2 = Data(date=date, subscribers=1500, reviews=220)

# db_session.add(row1)
# db_session.add(row2)
# db_session.commit()

print(db_session.query(Data).all()[0].subscribers)
datum = db_session.query(Data).all()[0]
datum.subscribers = 10000
# print(datum)
# db_session.add(datum)
# db_session.commit()

datum = db_session.query(Data).filter_by(subscribers=10000).one()
print(datum.subscribers)

db_session.delete(datum)
db_session.commit()