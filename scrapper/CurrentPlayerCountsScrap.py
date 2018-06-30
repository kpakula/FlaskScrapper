from urllib.request import Request
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from items.CPlayer import CPlayer
import re
from extensions.CSV import CSVMaker
from strings import strings, scrapstrings
import _thread


class CurrentPlayerCount:
    headers = "id, game_title, steam_id, steam_link, current_users, peak24, alltimepeak\n"

    def __init__(self):
        self.filename = strings.filename_current_players
        self.my_url = scrapstrings.steam_current_players
        self.regex_container = re.compile(r'app.*')
        self.user_agent = scrapstrings.user_agent
        self.regexID = re.compile(r'\/.[0-9]*.\/')
        self.objects = []

    def scrap(self):
        client = Request(self.my_url, headers={"User-Agent": self.user_agent})
        page_html = urlopen(client).read()
        page_soup = soup(page_html, "html.parser")
        containers = page_soup.findAll("tr", {"class": self.regex_container})
        return containers

    def get_objects(self):
        return self.objects

    def initialization(self):
        containers = self.scrap()
        i = 0
        for container in containers:
            if i < 50:
                playerCount = CPlayer()
                steam_link = container.a['href']
                steam_id_regex = self.regexID.findall(steam_link)
                steam_id = (steam_id_regex[0])[1:-1]
                info_container = container.findAll("td")
                game_title = info_container[2].text
                current_users = info_container[3].text
                peak24 = info_container[4].text
                alltimepeak = info_container[5].text

                playerCount.id = i + 1
                playerCount.steam_link = self.replace(steam_link)
                playerCount.steam_id = self.replace(steam_id)
                playerCount.game_title = self.replace(game_title)
                playerCount.current_users = self.replace(current_users)
                playerCount.peak24 = self.replace(peak24)
                playerCount.alltimepeak = self.replace(alltimepeak)

                self.objects.append(playerCount)
                # print("Steam link: " + steam_link)
                # print("Steam id: " + steam_id)
                # print("Game title: " + game_title)
                # print("Current users " + current_user)
                # print("Peak24 " + peak24)
                # print("Alltimepeak " + alltimepeak)
                # print("-----------------------------")
                i += 1
            else:
                break

        c = CSVMaker(self.headers, self.objects, self.filename)
        _thread.start_new_thread(c.makeCSV, (2,))

    def replace(self, s):
        return s.replace(",", ".")