"""Write a Python program to print 
yesterday, today, tomorrow."""
from datetime import datetime, date,timedelta

print(datetime.now()+timedelta(days=-1))
print(datetime.now())
print(datetime.now()+timedelta(days=+1))