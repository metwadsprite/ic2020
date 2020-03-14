from APIWrapper import APIWrapper
from utils import Point
from PlaneGame import PlaneGame
import json

with open('weights') as heatmap_file:
    heatmap = json.loads(heatmap_file.readline())

heatmap = sorted(heatmap, key=heatmap.get, reverse=True)

api_wrap = APIWrapper()
api_wrap.get_games()

# game = PlaneGame(api_wrap, heatmap, 120)
# game.run()
# print(game.attempt)

# game = PlaneGame(api_wrap, heatmap, 131)
# game.run()
# print(game.attempt)

for game in api_wrap.games[9:]:
    game = PlaneGame(api_wrap, heatmap, game)
    game.run()
    print(game.attempt)