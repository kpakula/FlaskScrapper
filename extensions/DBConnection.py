import mysql.connector
from strings import dbdata


class DatabaseController:
    addGame = ("INSERT INTO steam_games "
               "(title, price, rating, discount, link, steam_id) "
               "VALUES (%s, %s, %s, %s, %s, %s)")

    addItem = ("INSERT INTO steam_items "
               "(item_title, game_title, quantity, price, image_link, link_steam) "
               "VALUES (%s, %s, %s, %s, %s, %s)")

    addCurrentPlayersCount = ("INSERT INTO steam_current_players "
                              "(game_title, steam_id, steam_link, current_users, peak24, alltimepeak) "
                              "VALUES (%s, %s, %s, %s, %s, %s)")

    deleteGame = ("TRUNCATE table steam_games")

    deleteSteamItems = ("TRUNCATE table steam_items")

    deleteCurrentPlayersCount = ("TRUNCATE table steam_current_players")

    def __init__(self):
        self.user = dbdata.user
        self.password = dbdata.password
        self.host = dbdata.host
        self.database = dbdata.database

    def insert_into_current_players(self, currentplayers):
        cnx = mysql.connector.connect(user=self.user, password=self.password,
                                      host=self.host, database=self.database)
        cursor = cnx.cursor()
        cursor.execute(self.deleteCurrentPlayersCount)
        for currentplayer in currentplayers:
            data_current_user = (currentplayer.game_title, currentplayer.steam_id, currentplayer.steam_link,
                                 currentplayer.current_users, currentplayer.peak24, currentplayer.alltimepeak)
            cursor.execute(self.addCurrentPlayersCount, data_current_user)

        cnx.commit()
        cursor.close()
        cnx.close()

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
            data_item = (item.item_name, item.game_title, item.quantity, item.price, item.image_link, item.link_steam)
            cursor.execute(self.addItem, data_item)

        cnx.commit()
        cursor.close()
        cnx.close
