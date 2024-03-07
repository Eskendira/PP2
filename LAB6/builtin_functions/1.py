"""Write a Python program with builtin
 function to multiply all the numbers in a list"""

def multi(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

list = [3,2,4]
result = multi(list)
print("result:",result)