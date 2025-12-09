"""Project Euler Problem 6: Sum Square Difference
Objective:
    Find the difference between the square of sum and sum of squares
    for natural numbers from 1 to n.
Formula:
    (1 + 2 + ... + n)^2 - (1^2 + 2^2 + ... + n^2)
Inputs:
    t (int): Number of test cases
    n (int): Upper limit for each test case
Output:
    For each test case, prints the difference between square of sum
    and sum of squares for numbers 1 to n.
"""

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        sum_of_squares = int((n * (n + 1) * (2*n + 1))/6)
        square_of_sum = int(((n * (n + 1))/2) ** 2)
        print(square_of_sum - sum_of_squares)
