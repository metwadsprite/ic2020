class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, value):
        if self.x == value.x and self.y == value.y: return True
        return False

    def __hash__(self):
        return self.x * 100 + ord(self.y)