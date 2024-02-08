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