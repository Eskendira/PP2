"""Write a Python program to subtract 
five days from current date."""
from datetime import datetime, date, timedelta
print(datetime.now()+timedelta(days=-5))