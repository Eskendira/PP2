"""import math
class Circle():
    def __init__(self,r) -> None:
        self.r=r
    def area(self):
        return math.pi*self.r**2
    
a=Circle(5)
print(a.area())"""

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

print(calculate_factorial(5))


        
