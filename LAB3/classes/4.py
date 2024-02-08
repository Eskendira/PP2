"""Write the definition of a Point class. Objects from this class should have a

a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points"""

import math
class Point():
    def __init__(self, x, y):
        self.x1 = x
        self.y1 = y
    
    def show(self):
        return self.x1, self.y1
    
    def move(self, x, y):
        self.x1 = x
        self.y1 = y
    
    def dist(self, x, y):
        return (int(math.sqrt((x - self.x1) **2 + (y - self.y1) ** 2)))