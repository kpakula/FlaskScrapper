from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup as soup

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
my_url = 'https://steamdb.info/sales/'

client = Request(my_url, headers={"User-Agent": user_agent})
page_html = urlopen(client).read()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("tr", {"class": "app appimg"})

for container in containers:
    link_steam = container.a
    game_title = container.find("a", {"class": "b"})
    price = container.find("td", {"class": "price-discount"})

    # print(link_steam)
    # print(game_title)
    # print(price)


