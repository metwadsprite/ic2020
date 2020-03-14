from utils import Point
from APIWrapper import APIWrapper


class PlaneGame:
    def __init__(self, api_wrapper: APIWrapper, heatmap, game_id):
        self.api_wrapper = api_wrapper
        self.heatmap = heatmap
        self.game_id = game_id

        self.tried = set()
        self.hit = set()
        self.heads = set()

        self.tried.add(Point(1, 'A'))
        self.tried.add(Point(10, 'A'))
        self.tried.add(Point(1, 'J'))
        self.tried.add(Point(10, 'J'))

        self.attempt = 0

    def get_best_point(self):
        if len(self.hit):
            if not len(self.heads):
                for point in self.hit:
                    if point.x + 1 <= 10:
                        new_point = Point(point.x + 1, point.y)
                        if new_point not in self.tried: return new_point
                    if ord(point.y) + 1 <= 74:
                        new_point = Point(point.x, chr(ord(point.y) + 1))
                        if new_point not in self.tried: return new_point
                    elif ord(point.y) - 1 >= 65:
                        new_point = Point(point.x, chr(ord(point.y) - 1))
                        if new_point not in self.tried: return new_point
                    elif point.x - 1 >= 1:
                        new_point = Point(point.x - 1, point.y)
                        if new_point not in self.tried: return new_point
            else:
                wings = 0
                wing1 = Point(0, 0)
                wing2 = 0
                for point in self.heads:
                    if point.x + 1 <= 10:
                        if ord(point.y) + 3 <= 74:
                            new_point = Point(point.x + 1, chr(ord(point.y) + 3))
                            if self.strike(new_point) == 1:
                                if wing1 == Point(0, 0):
                                    wing1 = new_point
                                    wings = 1
                                else:
                                    if wing1.x == new_point.x or wing1.y == new_point.y:
                                        wing2 = new_point
                                        wings = 2
                                    else: wing1 = new_point
                        elif ord(point.y) - 3 >= 65:
                            new_point = Point(point.x + 1, chr(ord(point.y) - 3))
                            if self.strike(new_point) == 1:
                                if wing1 == Point(0, 0):
                                    wing1 = new_point
                                    wings = 1
                                else:
                                    if wing1.x == new_point.x or wing1.y == new_point.y:
                                        wing2 = new_point
                                        wings = 2
                                    else: wing1 = new_point
                    elif point.x - 1 >= 1:
                        if ord(point.y) + 3 <= 74:
                            new_point = Point(point.x - 1, chr(ord(point.y) + 3))
                            if self.strike(new_point) == 1:
                                if wing1 == Point(0, 0):
                                    wing1 = new_point
                                    wings = 1
                                else:
                                    if wing1.x == new_point.x or wing1.y == new_point.y:
                                        wing2 = new_point
                                        wings = 2
                                    else: wing1 = new_point
                        elif ord(point.y) - 3 >= 65:
                            new_point = Point(point.x - 1, chr(ord(point.y) - 3))
                            if self.strike(new_point) == 1:
                                if wing1 == Point(0, 0):
                                    wing1 = new_point
                                    wings = 1
                                else:
                                    if wing1.x == new_point.x or wing1.y == new_point.y:
                                        wing2 = new_point
                                        wings = 2
                                    else: wing1 = new_point

                    if point.x + 3 <= 10:
                        if ord(point.y) + 1 <= 74:
                            new_point = Point(point.x + 3, chr(ord(point.y) + 1))
                            if self.strike(new_point) == 1:
                                if wing1 == Point(0, 0):
                                    wing1 = new_point
                                    wings = 1
                                else:
                                    if wing1.x == new_point.x or wing1.y == new_point.y:
                                        wing2 = new_point
                                        wings = 2
                                    else: wing1 = new_point
                        elif ord(point.y) - 1 >= 65:
                            new_point = Point(point.x + 3, chr(ord(point.y) - 1))
                            if self.strike(new_point) == 1:
                                if wing1 == Point(0, 0):
                                    wing1 = new_point
                                    wings = 1
                                else:
                                    if wing1.x == new_point.x or wing1.y == new_point.y:
                                        wing2 = new_point
                                        wings = 2
                                    else: wing1 = new_point
                    elif point.x - 3 >= 1:
                        if ord(point.y) + 1 <= 74:
                            new_point = Point(point.x - 3, chr(ord(point.y) + 1))
                            if self.strike(new_point) == 1:
                                if wing1 == Point(0, 0):
                                    wing1 = new_point
                                    wings = 1
                                else:
                                    if wing1.x == new_point.x or wing1.y == new_point.y:
                                        wing2 = new_point
                                        wings = 2
                                    else: wing1 = new_point
                        elif ord(point.y) - 1 >= 65:
                            new_point = Point(point.x - 3, chr(ord(point.y) - 1))
                            if self.strike(new_point) == 1:
                                if wing1 == Point(0, 0):
                                    wing1 = new_point
                                    wings = 1
                                else:
                                    if wing1.x == new_point.x or wing1.y == new_point.y:
                                        wing2 = new_point
                                        wings = 2
                                    else: wing1 = new_point
                
                    # here
                    if wings >= 2:
                        if wing1.x == point.x + 3:
                            for i in range(ord(point.y) - 2, ord(point.y) + 2):
                                self.tried.add(Point(point.x + 1, chr(i)))
                            if wing2.y == chr(ord(point.y) + 1):
                                for i in range(point.x, point.x + 3):
                                    self.tried.add(Point(i, point.y))
                            elif wing2.y == chr(ord(point.y) - 1):
                                for i in range(point.x, point.x + 3):
                                    self.tried.add(Point(i, point.y))
                        elif wing1.x == point.x - 3:
                            for i in range(ord(point.y) - 2, ord(point.y) + 2):
                                self.tried.add(Point(point.x - 1, chr(i)))
                            if wing2.y == chr(ord(point.y) + 1):
                                for i in range(point.x - 3, point.x):
                                    self.tried.add(Point(i, point.y))
                            elif wing2.y == chr(ord(point.y) - 1):
                                for i in range(point.x - 3, point.x):
                                    self.tried.add(Point(i, point.y))
                        elif wing1.x == point.x + 1:
                            if wing2.y == chr(ord(point.y) + 3):
                                for i in range(point.x - 2, point.x + 2):
                                    self.tried.add(Point(i, chr(ord(point.y) + 1)))
                                for i in range(ord(point.y), ord(point.y) + 3):
                                    self.tried.add(Point(point.x, chr(i)))
                            elif wing2.y == chr(ord(point.y) - 3):
                                for i in range(point.x - 2, point.x + 2):
                                    self.tried.add(Point(i, chr(ord(point.y) - 1)))
                                for i in range(ord(point.y) - 3, ord(point.y)):
                                    self.tried.add(Point(point.x, chr(i)))
                        elif wing1.x == point.x - 1:
                            if wing2.y == chr(ord(point.y) + 3):
                                for i in range(point.x - 2, point.x + 2):
                                    self.tried.add(Point(i, chr(ord(point.y) + 1)))
                                for i in range(ord(point.y), ord(point.y) + 3):
                                    self.tried.add(Point(point.x, chr(i)))
                            elif wing2.y == chr(ord(point.y) - 3):
                                for i in range(point.x - 2, point.x + 2):
                                    self.tried.add(Point(i, chr(ord(point.y) - 1)))
                                for i in range(ord(point.y) - 3, ord(point.y)):
                                    self.tried.add(Point(point.x, chr(i)))
        
        # use heatmap
        for coord in self.heatmap:
            coord = coord.split(':')
            x = int(coord[1])
            y = coord[0]

            point = Point(x, y)
            if point not in self.tried: return point

    def run(self):
        while len(self.heads) != 3:
            point = self.get_best_point()
            self.strike(point)

    def strike(self, point):
        if point not in self.tried:
            hit = self.api_wrapper.shoot(self.game_id, point)
            
            if int(hit) >= 0: self.tried.add(point)
            if int(hit) >= 1: self.hit.add(point)
            if int(hit) == 2: self.heads.add(point)

            self.attempt += 1

            return int(hit)
        elif point in self.heads: return 2
        elif point in self.hit: return 1
        elif point in self.tried: return 0