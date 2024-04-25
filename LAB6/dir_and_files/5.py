"""Write a Python program to write a list to a file."""

import os
items = ['Mango', 'Orange', 'Apple', 'Lemon']
file = open('work.txt','w')
file.writelines(items)
file.close()