"""
input
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

#https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter

{3} Exactly 3 occurrences;
{3,} At least 3 occurrences;
{,3} At most 3 occurrences;
{2,3} 2 to 3 occurrences.
"""
import re

def fun(s):
    # return True if s is a valid email, else return False
    return re.match('^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{,3}$',s)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)


