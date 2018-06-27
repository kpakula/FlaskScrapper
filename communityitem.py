class SteamItem:

    def __init__(self, item_name="-", game_title="-", quantity="-", price="-", image_link="-"):
        self._item_name = item_name
        self._game_title = game_title
        self._quantity = quantity
        self._price = price
        self._image_link = image_link

    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, item_name):
        self._item_name = item_name

    @item_name.deleter
    def item_name(self):
        del self._item_name

    @property
    def game_title(self):
        return self._game_title

    @game_title.setter
    def game_title(self, game_title):
        self._game_title = game_title

    @game_title.deleter
    def game_title(self):
        del self._game_title

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @quantity.deleter
    def quantity(self):
        del self._quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @price.deleter
    def price(self):
        del self._price

    @property
    def image_link(self):
        return self._image_link

    @image_link.setter
    def image_link(self, image_link):
        self._image_link = image_link

    @image_link.deleter
    def image_link(self):
        del self._image_link
