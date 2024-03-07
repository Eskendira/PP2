"""Write a Python program with builtin function that accepts a string and calculate the number 
of upper case letters and lower case letters"""
import re
def calc_up_low_case(str):
    up_count = len(re.findall(r'[A-Z]',str))
    low_count = len(re.findall(r'[a-z]',str))
    return up_count,low_count

str = "NUray NuRlaNkyzy"
calc_up_low_case()