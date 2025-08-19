def print_rangoli(size):
    for i in reversed(range(1,size+1)):
        for j in range(i,size+1):
            pattern = chr(96+j)+'-'+pattern+'-'+chr(96+j) if i<j else chr(96+j)
        print(pattern.center((n+n-1)*2-1,'-'))
    # noinspection PyInterpreter
    for i in range(2,size+1):
        for j in range(i,size+1):
            pattern = chr(96+j)+'-'+pattern+'-'+chr(96+j) if i<j else chr(96+j)
        print(pattern.center((n+n-1)*2-1,'-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)