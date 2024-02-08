"""Define a class named Shape and its subclass Square. 
The Square class has an init function which takes a length as argument.
 Both classes have a area function which can print the area of the shape 
 where Shape's area is 0 by default."""

class Square:
    def __init__(self, length ):
        self.length  = length

    def area (self):
        print(self.length * self.length == 0)  

class Shape(Square):
    def __init__(self, length = 0 ):
        self.length  = length
    
    def area (self) :
        print(self.length * self.length) 

p = Shape(4)
p.area()
# 3
class Rectangle(Shape):

    def __init__(self, length,  width):
        self.length = length
        self.width = width

    def area (self):
        print( self.length  * self.width)  


p = Rectangle(6,4)
p.area()

    
