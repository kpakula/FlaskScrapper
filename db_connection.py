import mysql.connector
import dbdata


class DatabaseController:
    addGame = ("INSERT INTO steam_games "
                "(title, price, rating, discount, link, steam_id) "
                "VALUES (%s, %s, %s, %s, %s, %s)")

    deleteGame = ("TRUNCATE table steam_games")

    deleteSteamItems = ("TRUNCATE table steam_items")

    addItem = ("INSERT INTO steam_items "
               "(item_title, game_title, quantity, price, image_link) "
               "VALUES (%s, %s, %s, %s, %s)")

    def __init__(self):
        print("sam sie tworze")
        self.user = dbdata.user
        self.password = dbdata.password
        self.host = dbdata.host
        self.database = dbdata.database

    def insert_into_games(self, gamelist):
        cnx = mysql.connector.connect(user=self.user, password=self.password,
                                      host=self.host, database=self.database)
        cursor = cnx.cursor()
        cursor.execute(self.deleteGame)
        for game in gamelist:
            data_game = (game.get_game_title(), game.get_price(), game.get_rating(),
                     game.get_discount(), game.get_link_steam(), game.get_steam_id())
            cursor.execute(self.addGame, data_game)

        cnx.commit()
        cursor.close()
        cnx.close()

    def insert_into_items(self, items):
        cnx = mysql.connector.connect(user=self.user, password=self.password,
                                      host=self.host, database=self.database)
        cursor = cnx.cursor()
        cursor.execute(self.deleteSteamItems)
        for item in items:
            data_item = (item.item_name, item.game_title, item.quantity, item.price, item.image_link)
            cursor.execute(self.addItem, data_item)

        cnx.commit()
        cursor.close()
        cnx.close
