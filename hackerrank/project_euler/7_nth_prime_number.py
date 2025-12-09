#!/bin/python3
"""Project Euler Problem 7: Nth Prime Number
Objective:
    Find the nth prime number for multiple test cases.
Inputs:
    t (int): Number of test cases
    n (int): Position of the prime number to find (1-indexed)
Output:
    For each test case, prints the nth prime number.
"""

def is_prime(num):
    """Check if a number is prime.
    Args:
        num (int): Number to check
    Returns:
        bool: True if num is prime, False otherwise
    """
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        i = 3
        factor = 0
        while i*i <=num:
            if num % i == 0:
                factor = i
                break
            i += 2
        if factor == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    t = int(input().strip())
    prime_array = []
    i = 2
    for t_itr in range(t):
        n = int(input().strip())
        while True:
            if len(prime_array) >= n:
                break
            prime_array.append(i) if is_prime(i) else 0
            i = i+1
        print(prime_array[n-1])
