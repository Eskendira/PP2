"""Write a Python program to copy the contents of a file to another file"""
import os
with open("work.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)

            