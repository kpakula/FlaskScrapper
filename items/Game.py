class Game:
    # A class to storing game data

    def __init__(self, identity="0", game_title="-", price="-", rating="-", link_steam="-", steam_id="-",
                 image_link="-"):
        self.discount = "90%"
        self.identity = identity
        self.game_title = game_title.replace(",", ".")
        self.price = price
        self.rating = rating
        self.link_steam = link_steam
        self.steam_id = steam_id
        self.image_link = image_link

    # getters

    def get_image_link(self):
        return self.image_link

    def get_discount(self):
        return self.discount

    def get_identity(self):
        return self.identity

    def get_game_title(self):
        return self.game_title

    def get_price(self):
        return self.price

    def get_rating(self):
        return self.rating

    def get_link_steam(self):
        return self.link_steam

    def get_steam_id(self):
        return self.steam_id

    # setters
    def set_image_link(self, image_link):
        self.image_link = image_link

    def set_discount(self, discount):
        self.discount = discount

    def set_identity(self, identity):
        self.identity = identity

    def set_game_title(self, game_title):
        self.game_title = game_title.replace(",", ".")

    def set_price(self, price):
        self.price = price

    def set_rating(self, rating):
        self.rating = rating

    def set_link_steam(self, link_steam):
        self.link_steam = link_steam

    def set_steam_id(self, steam_id):
        self.steam_id = steam_id
