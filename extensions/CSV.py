from strings import strings
import os


class CSVMaker:

    def __init__(self, headers, objects, filename):
        self.headers = headers
        self.objects = objects
        self.filename = filename
        self.save_path = strings.save_path
        self.complete_path = os.path.join(self.save_path, self.filename)

    # 1 - TOP 100 sales
    # 2 - Current users
    # 3 - Top 10 common items

    def makeCSV(self, mode):
        f = open(self.complete_path, "w")
        f.write(self.headers)

        if mode == 1:
            i = 0
            while i < len(self.objects):
                game = self.objects[i]
                f.write(
                    game.get_identity() + "," + game.get_game_title() + "," + game.get_price() + "," + game.get_rating() + "," + game.get_discount() + "," + game.get_link_steam() + "," + game.get_steam_id() + "\n")
                i += 1
        elif mode == 2:
            i = 0
            while i < len(self.objects):
                c = self.objects[i]
                f.write(
                    str(c.id) + "," + c.game_title + "," + c.steam_id + "," + c.steam_link + "," + c.current_users + "," + c.peak24 + "," + c.alltimepeak + "\n"
                )
                i += 1
        elif mode == 3:
            i = 0
            while i < len(self.objects):
                item = self.objects[i]
                f.write(
                    item.game_title + "," + item.item_name + "," + item.link_steam + "," + item.price + "," + item.quantity + "\n"
                )
                i += 1

        f.close()
