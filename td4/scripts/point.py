import math as m

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return (self.x, self.y)
    
    def move(self, x, y):
        self.x += x
        self.y += y

    def dist(self, other):
        """
        :param other: le point pour calculer la distance avec.
        """
        dx = other.x - self.x
        dy = other.y - self.y
        return m.sqrt(dx ** 2 + dy ** 2)