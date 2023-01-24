from bs4 import BeautifulSoup
import requests


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

movies = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
movies.reverse()

with open("movies.txt", "w") as file:
    file.writelines(movie + "\n" for movie in movies)
    print("write success")

# with open("100movies.txt", mode="w") as file:
#     for movie in movies:
#         file.write(movie + "\n")
#     print("success")
