from bs4 import BeautifulSoup
import requests
import datetime
from assets.database import db_session
from assets.models import Data

def get_udemy_info():
    URL = "https://scraping-for-beginner.herokuapp.com/udemy"
    res = requests.get(URL)

    soup = BeautifulSoup(res.text, "html.parser")
    name_data = soup.select("body > div.row > div > div:nth-child(2) > div > div > div.card-image > span")
    name = name_data[0].string

    students = soup.select("body > div.row > div > div:nth-child(2) > div > div > div.card-action > p.subscribers")
    students_string = students[0].string
    students_split = students_string.split("：")[1]
    students_num = int(students_split)

    reviews = soup.select("body > div.row > div > div:nth-child(2) > div > div > div.card-action > p.reviews")
    reviews_string = reviews[0].string
    reviews_split = reviews_string.split("：")[1]
    reviews_num = int(reviews_split)

    results = {"name": name, "n_students": students_num, "n_reviews": reviews_num}
    return results

def write_data():
    # df = pd.read_csv("assets/data.csv")
    _results = get_udemy_info()

    date = datetime.datetime.today().strftime('%Y/%-m/%-d')
    subscribers = _results['n_students']
    review = _results['n_reviews']

    # results = pd.DataFrame([[date, subscribers, review]], columns=["date", 'subscribers', 'reviews'])

    # df = pd.concat([df, results])
    # df.to_csv("assets/dataout.csv", index=False)
    row = Data(date=date, subscribers=subscribers, reviews=review)

if __name__ == "__main__":
    write_data()