from bs4 import BeautifulSoup
import requests

URL = "https://scraping-for-beginner.herokuapp.com/udemy"

res = requests.get(URL)
# print(res.status_code)

soup = BeautifulSoup(res.text, "html.parser")
# print(soup)
name = soup.select("body > div.row > div > div:nth-child(2) > div > div > div.card-image > span")
print("Name: " + name[0].string)

students = soup.select("body > div.row > div > div:nth-child(2) > div > div > div.card-action > p.subscribers")
students_string = students[0].string
students_split = students_string.split("：")[1]
print(type(students_split))
print(int(students_split))
# print("Student number: " + int(students_split))

reviews = soup.select("body > div.row > div > div:nth-child(2) > div > div > div.card-action > p.reviews")
reviews_string = reviews[0].string
reviews_split = reviews_string.split("：")[1]
print(int(reviews_split))