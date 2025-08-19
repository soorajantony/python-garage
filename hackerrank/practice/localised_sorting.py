# Your task is to sort the string  in the following manner:
#
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.
#
# input : Sorting1234
# output : ginortS1324


chars = sorted(input())
chars.sort(key=lambda x: (x.isdigit(), x.isupper(), x.islower(), x in "24680"))
print(*chars, sep="")

# if the sort keys are same, it will be sorted based on the value

#https://www.hackerrank.com/challenges/ginorts/problem