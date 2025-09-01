"""
Project Euler Problem 3: Largest Prime Factor

Objective: Find the largest prime factor of given numbers.

Input:
- First line: t (number of test cases)
- Next t lines: n (positive integer for each test case)

Output: The largest prime factor of each n

Example: For n = 13195, prime factors are 5, 7, 13, 29
Largest prime factor = 29
"""

def largest_prime_factor(n):
    largest = 1
    i = 2
    while i * i <= n:
        while n % i == 0:
            largest = i
            n //= i
        i += 1
    if n > 1:
        largest = n
    print(largest)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        largest_prime_factor(n)
