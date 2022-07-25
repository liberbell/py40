from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

URL = "https://scraping-for-beginner.herokuapp.com/udemy"

res = requests.get(URL)
# print(res.status_code)

soup = BeautifulSoup(res.text, "html.parser")
# print(soup)
name_data = soup.select("body > div.row > div > div:nth-child(2) > div > div > div.card-image > span")
name = name_data[0].string
# print(name)

students = soup.select("body > div.row > div > div:nth-child(2) > div > div > div.card-action > p.subscribers")
students_string = students[0].string
students_split = students_string.split("：")[1]
students_num = int(students_split)
# print(type(students_split))
# print(int(students_split))
# print("Student number: " + int(students_split))

reviews = soup.select("body > div.row > div > div:nth-child(2) > div > div > div.card-action > p.reviews")
reviews_string = reviews[0].string
reviews_split = reviews_string.split("：")[1]
reviews_num = int(reviews_split)
# print(int(reviews_split))

results = {"name": name, "n_students": students_num, "n_reviews": reviews_num}
print(results)

df = pd.read_csv("assets/data.csv")
# print(df.head())
# print(df.tail())

# print(datetime.datetime.today().strftime('%Y/%-m/%-d'))
date = datetime.datetime.today().strftime('%Y/%-m/%-d')

subscribers = results['n_students']
review = results['n_reviews']

print(subscribers, review)

print(pd.DataFrame([[date, subscribers, review]], columns=["date", 'subscribers', 'reviews']))