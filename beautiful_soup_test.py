import requests
import bs4

res = requests.get("https://www.nostarch.com")
res.raise_for_status()
no_starch_soup = bs4.BeautifulSoup(res.text)
print(type(no_starch_soup))

example_file = open("example.html")
example_soup = bs4.BeautifulSoup(example_file)
print(type(example_soup))
