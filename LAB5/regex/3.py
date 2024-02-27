"""Write a Python program to find sequences of
 lowercase letters joined with a underscore."""
import re
txt = "ab_bbb"
x = re.findall(r'[a-z]+_[a-z]+',txt)
print(x)

