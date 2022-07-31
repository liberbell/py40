from assets.database import db_session
from assets.models import Data
import pandas as pd

data = db_session.query(Data.date, Data.subscribers, Data.reviews).all()
print(data[0].date)

dates = []
subscribers = []
reviews = []
for datum in data:
    dates.append(datum.date)
    subscribers.append(datum.subscribers)
    reviews.append(datum.reviews)
    # print(dates)

diff_subscribers = pd.Series(subscribers).diff()
diff_reviews = pd.Series(subscribers).diff()
