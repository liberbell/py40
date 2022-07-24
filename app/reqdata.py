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
students_split = students_string.split("：")
print("Student number: " + students_split[1])

reviews = soup.select("body > div.row > div > div:nth-child(2) > div > div > div.card-action > p.reviews")
print(reviews[0].string)