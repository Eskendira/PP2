"""Write a function that computes the volume of a sphere given its radius."""

import math      
def sphere(r):
    return (4/3)*3.1415*math.pow(r,3)
r=int(input("radius:"))
print("volume of the sphere:",sphere(r))