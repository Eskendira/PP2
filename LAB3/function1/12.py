"""Define a functino histogram() 
that takes a list of integers and prints a histogram to the screen. 
For example, histogram([4, 9, 7]) should print the following:"""

def histogram(ls):
    s = ''
    for i in range(0, len(ls)):
        for x in range(0, ls[i]):
            x = '*'
            s += x
        print(s)
histogram([3,5,6])

