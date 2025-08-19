"""
Project Euler Problem 1: Multiples of 3 and 5

Objective: Find the sum of all multiples of 3 or 5 below n
Solution: Uses O(1) arithmetic progression formula for fast execution
"""

def sum_calculation(n, factor):
    """
    Calculate sum of arithmetic progression: factor + 2*factor + 3*factor + ... + k*factor
    where k*factor < n using the formula: factor * k * (k + 1) / 2
    
    Args:
        n (int): Upper limit (exclusive)
        factor (int): The multiple to sum
    
    Returns:
        int: Sum of multiples of factor below n
    """
    k = (n-1) // factor  # Number of multiples of factor below n
    return k * (k + 1) // 2

# Read number of test cases
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    # Calculate sum of multiples using inclusion-exclusion principle
    sum_3 = 3 * sum_calculation(n, 3)    # Sum of multiples of 3
    sum_5 = 5 * sum_calculation(n, 5)    # Sum of multiples of 5
    sum_15 = 15 * sum_calculation(n, 15) # Sum of multiples of 15 (3*5)
    
    # Apply inclusion-exclusion: |A ∪ B| = |A| + |B| - |A ∩ B|
    print(sum_3 + sum_5 - sum_15)
