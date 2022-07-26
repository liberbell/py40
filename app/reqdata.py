from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

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

def 

df = pd.read_csv("assets/data.csv")

date = datetime.datetime.today().strftime('%Y/%-m/%-d')

subscribers = results['n_students']
review = results['n_reviews']

results = pd.DataFrame([[date, subscribers, review]], columns=["date", 'subscribers', 'reviews'])

df = pd.concat([df, results])
# print(df.tail())
df.to_csv("assets/data.csv", index=False)