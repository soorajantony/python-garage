#!/bin/python3
"""
Project Euler Problem 2: Even Fibonacci Numbers

Objective: Find the sum of all even-valued terms in the Fibonacci sequence
whose values do not exceed n.

Input:
- First line: t (number of test cases)
- Next t lines: n (upper limit for each test case)

The Fibonacci sequence: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Even terms: 2, 8, 34, ...
"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        val_0 = 0
        val_1 = 1
        fib_list = []
        fib_sum = 0
        while True:
            if val_0 > n:
                break
            fib_sum = fib_sum + val_0 if val_0 % 2 == 0 else fib_sum
            if val_1 > n:
                break
            fib_sum = fib_sum + val_1 if val_1 % 2 == 0 else fib_sum
            val_0 = val_0 + val_1
            val_1 = val_0 + val_1
        print(fib_sum)
