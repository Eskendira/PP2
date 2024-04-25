"""Write a Python program to check for access to a specified path. Test the existence, readability, writability
 and executability of the specified path"""

import os

path=r'C:\Users\User\Music\PP2\lab 6\dir-and-files'

print(os.access(path,os.F_OK))

print(os.access(path,os.R_OK))

print(os.access(path,os.W_OK))

print(os.access(path,os.X_OK))