"""Write a Python program to calculate
 the area of regular polygon."""

import math 
a=int(input('Input number of sides:'))
b=int(input('Input the length of a side:'))
print('The area of polygon is :',int((pow(b,2)*a)/(4*math.tan((math.pi/a)))),sep='')
      
      