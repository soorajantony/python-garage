#specifications:
#Mat size must be X. ( is an odd natural number, and  is  times .)
#The design should have 'WELCOME' written in the center.
#The design pattern should only use |, . and - characters.


row, col = list(map(int, input().split()))
for i in range(1,row):
    if i%2 !=0:
        print(str('.|.'*i).center(col,'-'))
print('WELCOME'.center(col,'-'))
for i in reversed(range(1,row)):
    if i%2 !=0:
        print(str('.|.'*i).center(col,'-'))