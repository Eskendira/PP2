"""Write a Python program to calculate 
two date difference in seconds."""
from datetime import date,datetime,timedelta,time
a = datetime.today()
b = datetime.strptime("2 March 2023,07:00:00","%d %B %Y,%H:%M:%S")
c = (a-b).seconds
print(datetime.today())
print(c)
