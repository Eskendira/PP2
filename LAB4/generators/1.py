"""Create a generator that generates 
the squares of numbers up to some number N."""
import math
def squares(n):
    for i in range(1 , n+1):
        print(pow(i,2))
squares(10)