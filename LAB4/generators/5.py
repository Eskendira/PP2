"""Implement a generator that returns all 
numbers from (n) down to 0."""

def gen(n):
    i=0
    while n>i:
        yield n
        n=n-1

for i in gen(int(input())):
    print(i)