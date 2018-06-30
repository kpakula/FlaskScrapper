from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup as soup
import re
from strings import strings, scrapstrings as connect_data
from items.Game import Game
import _thread
from extensions.CSV import CSVMaker


class Scrap:
    headers = "id, title, price, rating, discount, link_steam, steam_id\n"

    def __init__(self):
        self.user_agent = connect_data.user_agent
        self.my_url = connect_data.steam_db_url
        self.regex_container = re.compile(r'app appimg.*')
        self.regexID = re.compile(r'\/.[0-9]*.\/')
        self.filename = strings.filename_sales
        self.save_path = strings.save_path
        self.objects = []

    def initialization(self):
        client = Request(self.my_url, headers={"User-Agent": self.user_agent})
        page_html = urlopen(client).read()
        page_soup = soup(page_html, "html.parser")
        containers = page_soup.findAll("tr", {"class": self.regex_container})
        obj = []
        id = 1;

        for container in containers:
            game = Game()
            game.set_link_steam(container.a['href'])
            steam_id_regex = self.regexID.findall(game.get_link_steam())
            game.set_steam_id((steam_id_regex[0])[1:-1])
            game.set_game_title(container.find("a", {"class": "b"}).text)
            game.set_discount('90%')

            info_container = container.findAll("td")

            game.set_price(info_container[4].text)
            game.set_rating(info_container[5].text)
            game.set_identity(str(id))

            id = id + 1
            obj.append(game)
        self.sortbyRating(obj)

        c = CSVMaker(self.headers, self.objects, self.filename)
        _thread.start_new_thread(c.makeCSV, (1,))

    def sortbyRating(self, obj):
        obj.sort(key=lambda x: x.rating, reverse=True)
        game = Game()
        i = 0
        while i < 99:
            game = obj[i]
            self.objects.append(game)
            i += 1

    def get_objects(self):
        return self.objects
