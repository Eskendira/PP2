"""write a func using regular expression to find all Kz phone num within given input 
.the phone num should match a pattern ,like +7-xxx-xxx-xx-xx  or 8 -xxx-xxx-xx-xx """

import re
x= r'(\+7|8)[ -]?\d{3}[ -]?\d{3}[ -]?\d{2}[ -]?\d{2}' 
     

txt = '8-775-84-28-40'
phones = re.search(x, txt) 
print(phones)




   



















   