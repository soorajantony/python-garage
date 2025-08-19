if __name__ == '__main__':
    N = int(input())
    result = []
    for _ in range(1,N+1):
        com = input().split()
        if com[0] == 'append':
            result.append(int(com[1]))
        elif com[0] == 'print':
            print(result)
        elif com[0] == 'remove':
            result.remove(int(com[1]))
        elif com[0] == 'insert':
            result.insert(int(com[1]), int(com[2]))
        elif com[0] == 'sort':
            result.sort()
        elif com[0] == 'pop':
            result.pop()
        elif com[0] == 'reverse':
            result.reverse()
        else:
            print('Incorrect Input')


"""
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""