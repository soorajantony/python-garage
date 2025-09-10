"""
Project Euler Problem 4: Largest Palindrome Product

Objective: Find the largest palindrome made from the product of two 3-digit numbers that is less than N.

Input:
- First line: t (number of test cases)
- Next t lines: N (upper bound for each test case)

Output: The largest palindrome product of two 3-digit numbers < N

Example: For N = 101110, products like 99*91=9009 (palindrome)
Largest palindrome < 101110 = 99009
"""

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        i = 999
        num_ans = 0
        while i >= 100:
            if n/i > 999:
                i_n = 999
            else:
                i_n = int((n-1)/i)
            for j in range(i_n, 100, -1):
                num = i * j
                str_num = str(num)
                if str_num == str_num[::-1]:
                    if num > num_ans:
                        num_ans = num
                    break
            i -= 1
        print(num_ans)
