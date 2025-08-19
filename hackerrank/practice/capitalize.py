def solve1(s):
    new_str = []
    flag = 'N'
    for i in s:
        if i.isalpha() and flag == 'N':
            new_str.append(i.upper())
            flag = 'Y'
        elif i == ' ':
            flag = 'N'
            new_str.append(i)
        else:
            new_str.append(i)
    print(''.join(new_str))

def solve2(s):
    new_str = []
    for i in s.split(" "):
        if i.isdigit():
            new_str.append(i)
        else:
            new_str.append(i.capitalize())
    print(' '.join(new_str))


solve1('12hello  world')   #capitalize when number is there
solve2('12hello  world')   # ignore when there is a number