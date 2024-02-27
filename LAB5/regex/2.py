"""Write a Python program that matches a string that
 has an 'a' followed by two to three 'b'."""

import re

def check_string(text):
    pattern = 'a{1}b{2,3}'
    if re.search(pattern , text):
        return 'match'
    else:
        return 'no match'
    
text = 'abb'
print(check_string(text))
    
