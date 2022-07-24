from bs4 import BeautifulSoup
import requests

URL = "https://scraping-for-beginner.herokuapp.com/udemy"

res = requests.get(URL)
# print(res.status_code)

soup = BeautifulSoup(res.text, "html.parser")
# print(soup)
res1 = soup.select("body > div.row > div > div:nth-child(2) > div > div > div.card-image > span")
print(res1[0].string)