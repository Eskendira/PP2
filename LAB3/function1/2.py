""" 2) Read in a Fahrenheit temperature.
Calculate and display the equivalent centigrade temperature. 
The following formula is used for the conversion: C = (5 / 9) * (F - 32)"""

def fahrenheit_to_centigrade(fahrenheit):
    centigrade = (5/9) * ( fahrenheit - 32)
    return centigrade
fahrenheit= float(input("Fahrenheit:"))
centigrade = fahrenheit_to_centigrade(fahrenheit)
print(fahrenheit,"^F","=",centigrade,"^C")