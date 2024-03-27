"""Write a Python program that invoke square root function
 after specific milliseconds.
Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858"""

import time
def square(x,y):
    x1 = x ** (1/2)
    time.sleep(y/1000)
    print(f'Square root of {x} after {y} miliseconds is {x1}')

square(25100, 2123)