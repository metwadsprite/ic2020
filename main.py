from APIWrapper import APIWrapper
from utils import Point

api_wrap = APIWrapper()
api_wrap.get_games()
print(api_wrap.games)
print(api_wrap.shoot(120, Point(1, 'A')))