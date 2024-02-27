"""Write a Python program that matches a string that
has an 'a'followed by zero or more 'b''s."""

import re

def check_string(text):
    pattern = 'ab*'
    if re.search(pattern, text):
        return 'match'
    else:
        return 'no match'

text = 'ggga'
print(check_string(text))
