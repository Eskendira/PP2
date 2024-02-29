"""Write a Python program to replace all occurrences 
of space, comma, or dot with a colon."""

import re
def space(txt):
    x = re.sub("\s",":",txt)
    y = re.sub('\.',':',x)
    print(y)

space('asfd kjf.. sd')