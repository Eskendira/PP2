"""Write a Python program to drop 
microseconds from datetime."""
from datetime import datetime, date,timedelta

def drop():
    print(datetime.now().replace(microsecond=0))

drop()