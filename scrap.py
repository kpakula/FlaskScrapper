from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup as soup
import re

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 " \
             "Safari/537.36 "
my_url = 'https://steamdb.info/sales/?min_discount=90&min_rating=0'

regex = re.compile(r'app appimg.*')


client = Request(my_url, headers={"User-Agent": user_agent})
page_html = urlopen(client).read()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("tr", {"class": regex})

filename = "discount.csv"
f = open(filename, "w")

headers = "title, price, rating, discount, link_steam\n"
f.write(headers)


for container in containers:
    link_steam = container.a['href']
    game_title = container.find("a", {"class": "b"}).text
    discount = '90%'
    info_container = container.findAll("td")
    price = info_container[4].text
    rating = info_container[5].text

    f.write(game_title.replace(",", ".") + "," + price + "," + rating + "," + discount + "," + link_steam + "\n")

f.close()
