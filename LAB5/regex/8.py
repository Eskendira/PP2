"""Write a Python program to split a string
 at uppercase letters."""

import re
txt = "SplitIt"
print(re.findall('[A-Z][^A-Z]*',txt))