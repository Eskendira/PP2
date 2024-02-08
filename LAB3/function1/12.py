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

"""We define a function called histogram that takes a list ls as its parameter.

Inside the function, we initialize an empty string s to store the histogram.

We use a nested loop to iterate over each element in the list ls. The outer loop iterates over the indices of the list, while the inner loop iterates ls[i] times.

In each iteration of the inner loop, we assign the value '*' to the variable x. This represents a single bar in the histogram.

We concatenate the x to the string s using the += operator.

After the inner loop finishes, we print the current state of the histogram string s.

Finally, we call the histogram function with a sample list [3, 5, 6] to generate the histogram.

The output of the code will be:"""