import scrapstrings as connect_data
from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from communityitem import SteamItem


class SteamScrap:

    def __init__(self):
        self.user_agent = connect_data.user_agent
        self.my_url = connect_data.steam_community_url
        self.div_class_name = "market_listing_row market_recent_listing_row market_listing_searchresult"
        self.objects = []

    def initialization(self):
        client = Request(self.my_url, headers={"User-Agent": self.user_agent})
        page_html = urlopen(client).read()
        page_soup = soup(page_html, "html.parser")
        containers = page_soup.findAll("div", {"class": self.div_class_name})

        for container in containers:
            item = SteamItem()
            item.image_link = container.find('img')['src']
            item.price = container.findAll("span", {"class": "normal_price"})[1].text
            item.quantity = container.findAll("span", {"class": "market_listing_num_listings_qty"})[0].text
            item.game_title = container.findAll("span", {"class": "market_listing_game_name"})[0].text
            item.item_name = container.findAll("span", {"class": "market_listing_item_name"})[0].text
            self.objects.append(item)

    def get_objects(self):
        return self.objects

    def get_object(self):
        return self.objects[0]