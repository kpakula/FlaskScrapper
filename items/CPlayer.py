class CPlayer:
    def __init__(self, identity=" ", steam_link="-", steam_id="-", game_title="-", current_users="-", peak24="-",
                 alltimepeak="-"):
        self.id = identity
        self.steam_link = steam_link
        self.steam_id = steam_id
        self.game_title = game_title
        self.current_users = current_users
        self.peak24 = peak24
        self.alltimepeak = alltimepeak
