from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup as soup
import re
from game import Game


class Scrap:

    def __init__(self):
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/60.0.3112.113 Safari/537.36 "
        self.my_url = 'https://steamdb.info/sales/?min_discount=90&min_rating=0'
        self.regex_container = re.compile(r'app appimg.*')
        self.regexID = re.compile(r'\/.[0-9]*.\/')
        self.filename = "discount.csv"
        self.objects = []

    def initialization(self):
        client = Request(self.my_url, headers={"User-Agent": self.user_agent})
        page_html = urlopen(client).read()
        page_soup = soup(page_html, "html.parser")
        containers = page_soup.findAll("tr", {"class": self.regex_container})

        try:
            f = open(self.filename, "w")

            headers = "id, title, price, rating, discount, link_steam, steam_id\n"
            f.write(headers)

            id = 1;

            for container in containers:
                game = Game()
                # link_steam = container.a['href']
                game.set_link_steam(container.a['href'])
                steam_id_regex = self.regexID.findall(game.get_link_steam())
                game.set_steam_id((steam_id_regex[0])[1:-1])
                game.set_game_title(container.find("a", {"class": "b"}).text)
                game.set_discount('90%')

                info_container = container.findAll("td")
                game.set_price(info_container[4].text)
                game.set_rating(info_container[5].text)
                game.set_id(str(id))

                f.write(game.get_id() + "," + game.get_game_title() + "," + game.get_price() + "," + game.get_price() +
                        "," + game.get_rating() + "," + game.get_link_steam() + "," + game.get_steam_id() + "\n")
                id = id + 1
                self.objects.append(game)

            f.close()

        except PermissionError:
            print("The .csv file is open")

    def get_objects(self):
        return self.objects

