import itertools
def permutation(s = str(input())):
    nums = list(s)
    permutations = list(itertools.permutations(nums))
    print([''.join(permutation) for permutation in permutations])
permutation()

"""We start by importing the itertools module, which provides various functions for efficient iteration.

Next, we define a function called permutation that takes a string s as input. We use the str(input()) function to prompt the user to enter a string. If no input is provided, the function will default to an empty string.

Inside the permutation function, we convert the input string s into a list of characters called nums. This allows us to easily iterate over the characters later.

We then use the itertools.permutations function to generate all possible permutations of the characters in nums. This function returns an iterator, so we convert it to a list using list().

Finally, we use a list comprehension to join each permutation of characters into a string and print the result. The [''.join(permutation) for permutation in permutations] expression iterates over each permutation in the permutations list, joins the characters together using join(), and creates a new list of strings.

Outside the permutation function, we call the function to execute it."""