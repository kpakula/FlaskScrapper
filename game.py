class Game:
    # A class to storing game data

    def __init__(self, id, game_title, price, rating, link_steam, steam_id):
        self.discount = "90%"
        self.id = id
        self.game_title = game_title.replace(",", ".")
        self.price = price
        self.rating = rating
        self.link_steam = link_steam
        self.steam_id = steam_id

    def __init__(self):
        self.discount = "0%"
        self.id = "-"
        self.game_title = "-"
        self.price = "-"
        self.rating = "-"
        self.link_steam = "-"
        self.steam_id = "-"

    # getters
    def get_discount(self):
        return self.discount

    def get_id(self):
        return self.id

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
    def set_discount(self, discount):
        self.discount = discount

    def set_id(self, id):
        self.id = id

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

