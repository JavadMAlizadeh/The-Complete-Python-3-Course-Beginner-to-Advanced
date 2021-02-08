#https://www.youtube.com/watch?v=87Gx3U0BDlo&ab_channel=freeCodeCamp.org

from bs4 import BeautifulSoup
import requests

search = input("Search for: ")
params = {"q": search}
result = requests.get("https://www.google.com/search?", params=params)
source = result.content
soup = BeautifulSoup(source, "html.parser")

for a in soup.find_all("a"):
    print(a.attrs["href"])

