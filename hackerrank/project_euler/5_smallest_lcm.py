"""
Project Euler Problem 5: Smallest Multiple

Objective: Find the smallest positive number that is evenly divisible by all numbers from 1 to N.

Input:
- First line: t (number of test cases)
- Next t lines: N (positive integer for each test case)

Output: The smallest multiple (LCM) of all numbers from 1 to N

Logic: Uses prime factorization approach - for each prime p ≤ N, 
find the highest power of p that is ≤ N, then multiply all such powers.

Example: For N = 10, primes are 2,3,5,7 with highest powers 8,9,5,7
LCM = 8 × 9 × 5 × 7 = 2520
"""

def smallest_prime_factor(num):
    #the smallest factor >1 of a prime is the number itself
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return i
    return num

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        result = 1
        # For each number from 2 to n
        for i in range(2, n + 1):
            # Find highest power of i's smallest prime factor
            p = smallest_prime_factor(i)
            if p == i:  # i is prime
                power = i
                while power * i <= n:
                    power *= i
                result *= power
        print(result)
