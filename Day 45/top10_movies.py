import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
html_text = response.text

soup = BeautifulSoup(html_text, "html.parser")

contents = soup.find_all(name='h3', class_="title")
contents.reverse()

for movie in contents:
    with open("movies.txt", "a") as f:
        f.write(f"{movie.getText()}\n")

