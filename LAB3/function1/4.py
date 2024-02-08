""" 4) You are given list of numbers separated by spaces.
Write a function filter_prime which will take list of numbers as an agrument
and returns only prime numbers from the list."""

def filter_prime(numbers):
    prime = []
    for num in numbers:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime.append(num)
    return prime

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime= filter_prime(numbers)
print(prime)


"""We define a function called filter_prime that takes a single parameter numbers, which represents the list of numbers we want to filter.

We initialize an empty list called prime_numbers to store the prime numbers we find.

We iterate over each number in the numbers list using a for loop.

Inside the loop, we check if the current number (num) is greater than 1. This is because prime numbers are defined as numbers greater than 1.

If the number is greater than 1, we enter another for loop that iterates from 2 to the current number (num). We start from 2 because every number is divisible by 1, so we skip it.

Inside the inner loop, we check if the current number (num) is divisible by any number in the range from 2 to num - 1. If it is divisible, we break out of the loop using the break statement.

If the inner loop completes without finding any divisors, it means the current number is prime. In this case, we append it to the prime_numbers list.

Finally, we return the prime_numbers list, which contains all the prime numbers from the input list."""