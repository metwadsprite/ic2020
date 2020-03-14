import requests as req

class APIWrapper:
    def __init__(self):
        self.url = "http://ic2020-laj-api.netrom.live"
        self.username = "la-jet-gang"
        self.password = "LwtJmz29mtn5J4J8"
        self.login_route = "login_check"
        self.game_list_route = "games"
        self.shoot_route = "game/{}/shoot"

        self.login()

    def login(self):
        headers = {
            'Content-Type': 'application/json'
        }
        credentials = {
            'username': self.username,
            'password': self.password
        }

        resp = req.post(url="{}/{}".format(self.url, self.login_route), headers=headers, json=credentials)
        self.token = resp.json()['token']
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token)
        }

    def get_games(self):
        resp = req.get(
            url='{}/{}'.format(self.url, self.game_list_route),
            headers=self.headers
        )
        self.games = resp.json()

    def shoot(self, game_id, point):
        content = {
            'x': point.x,
            'y': point.y
        }

        resp = req.post(
            url='{}/{}'.format(self.url, self.shoot_route.format(game_id)),
            headers=self.headers,
            json=content
        )
        return resp.json()['code']