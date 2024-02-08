import itertools
def permutation(s = str(input())):
    nums = list(s)
    permutations = list(itertools.permutations(nums))
    print([''.join(permutation) for permutation in permutations])
permutation()

