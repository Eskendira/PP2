"""Define a class which has at least two methods:
getString: to get a string from console input printString: 
to print the string in upper case."""


class string():
    def __init__(s):
        s.s=""
    def getstring(s):
        s.s = str(input())
    def printstring(s):
        print(s.s.upper())

p = string()
p.getstring()
p.printstring()
