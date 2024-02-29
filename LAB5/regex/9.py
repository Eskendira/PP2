"""Write a Python program to insert spaces between words 
starting with capital letters."""

import re

def i_space(txt):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", txt)

print(i_space('CapitalLetter'))