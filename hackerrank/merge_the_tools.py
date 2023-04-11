def merge_the_tools(string, k):
    c = 0
    sub_list = []
    for i in range(len(string)):
        sub_list.append(string[i])
        if (i+1) % k == 0:
            print(''.join(list(dict.fromkeys(sub_list))))
            sub_list = []


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)



#https://www.hackerrank.com/challenges/merge-the-tools/problem

#input
#AABCAAADA
#3