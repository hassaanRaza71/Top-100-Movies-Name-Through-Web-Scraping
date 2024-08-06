import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Fetch the webpage
response = requests.get(URL)
web_page = response.text

# Parse the webpage content
soup = BeautifulSoup(web_page, "html.parser")

# Extract movie titles
movie_list = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]

# Write the movie titles to a file in reverse order with UTF-8 encoding
with open("./Starting Code - 100 movies to watch start/movies.txt", "a", encoding="utf-8") as file:
    for movie in reversed(movie_list):
        file.write(movie + "\n")
