"""Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False"""


def spy_game(nums):
    for i in range (len(nums) - 2):
        if nums[i] == 0 and nums[i+1] == 0 and nums [i+2] == 7:
            return True
    return False


print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0])) 

"""The function spy_game is defined with a single parameter nums, which represents the list of integers.

Inside the function, we use a for loop to iterate over the list. The loop runs from the first element to the third-to-last element, as we need to check each element and the next two elements.

Within the loop, we use an if statement to check if the current element, the next element, and the element after that form the sequence "007". We do this by comparing nums[i] with 0, nums[i+1] with 0, and nums[i+2] with 7.

If the if condition is satisfied, we immediately return True, as we have found the sequence "007" in order.

If the loop completes without finding the sequence, we reach the return statement outside the loop, which returns False.

Finally, we test the function by calling it with different lists of integers and printing the results."""