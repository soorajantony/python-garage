def wrapper(f):
    def fun(l):
        f(list('+91 '+i[-10:-5]+' '+i[-5:] for i in l))    #decorator function calls the regular function from inside
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)


#https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem

#Input
#3
#07895462130
#919875641230
#9195969878