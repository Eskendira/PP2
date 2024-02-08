"""Define a class named Shape and its subclass Square. 
The Square class has an init function which takes a length as argument.
 Both classes have a area function which can print the area of the shape 
 where Shape's area is 0 by default."""

class Shape:
    def __init__(self):
        self.area = 0

    def area(self):
        print("The area of the shape is:", self.area)


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        self.area = self.length ** 2
        print("The area of the square is:", self.area)


shape = Shape()
square = Square(5)
shape.calculate_area()
square.calculate_area()


    
