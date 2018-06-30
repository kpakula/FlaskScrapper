from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from items.SteamMarketItem import SteamItem
from strings import strings, scrapstrings as connect_data
import _thread
from extensions.CSV import CSVMaker


class SteamScrap:
    headers = "game_title, item_name, link_steam, price, quantity\n"

    def __init__(self):
        self.filename = strings.filename_common_items
        self.user_agent = connect_data.user_agent
        self.my_url = connect_data.steam_community_url
        self.div_class_name = "market_listing_row market_recent_listing_row market_listing_searchresult"
        self.div_link_steam = "market_listing_row_link"
        self.objects = []

    def scrap(self):
        client = Request(self.my_url, headers={"User-Agent": self.user_agent})
        page_html = urlopen(client).read()
        page_soup = soup(page_html, "html.parser")
        return page_soup

    def initialization(self):
        page_soup = self.scrap()
        containers = page_soup.findAll("div", {"class": self.div_class_name})
        link_steam = page_soup.findAll("a", {"class": self.div_link_steam})
        i = 0
        for container in containers:
            item = SteamItem()
            item.price = self.replace(container.findAll("span", {"class": "normal_price"})[1].text)
            item.quantity = self.replace(container.findAll("span", {"class": "market_listing_num_listings_qty"})[0].text)
            item.game_title = self.replace(container.findAll("span", {"class": "market_listing_game_name"})[0].text)
            item.item_name = self.replace(container.findAll("span", {"class": "market_listing_item_name"})[0].text)
            item.link_steam = self.replace(link_steam[i]['href'])

            if i == 0:
                item.image_link = self.get_image(item.link_steam)
            self.objects.append(item)
            i += 1

        c = CSVMaker(self.headers, self.objects, self.filename)
        _thread.start_new_thread(c.makeCSV, (3,))

    def get_image(self, link):
        client = Request(link, headers={"User-Agent": self.user_agent})
        page_html = urlopen(client).read()
        page_soup = soup(page_html, "html.parser")
        s_link = page_soup.findAll("div", {"class": "market_listing_largeimage"})
        finallink = s_link[0].find('img')['src']
        return finallink

    def get_objects(self):
        return self.objects

    def get_object(self):
        return self.objects[0]

    def replace(self, s):
        return s.replace(",", ".")