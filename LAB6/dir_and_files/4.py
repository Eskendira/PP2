"""Write a Python program to count the number of lines in a text file."""


f=open("work.txt","r")
print(len(f.readlines()))

f.close()