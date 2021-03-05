import sys

input = sys.stdin.readline

Test_ = int(input())

while Test_ > 0:
    Test_ -= 1
    total_fun = input()
    length = int(input())

    if length == 0:
        trash = input()
        if 'D' in total_fun:
            print('error')
        else:
            print('[]')
        continue

    lst = list(map(int, input().replace('[','').replace(']','').replace('\n','').split(',')))
    check = False
    check_rev = 0
    for fun in total_fun:
        # print("lst = ", lst)
        if len(lst) == 0 and fun == 'D':
            print('error')
            check = True
            break 
        if fun == 'R':
            if check_rev == 0:
                check_rev = 1
            else:
                check_rev = 0
        elif fun == 'D':
            if check_rev == 1:
                lst.pop()
            else:
                lst.pop(0)
        
    if not check:
        if check_rev == 1:
            lst.reverse()

        answer = ''
        for i in range(len(lst)):
            if i == len(lst)-1:
                answer += str(lst[i])
            else:
                answer += str(lst[i]) + ','
        print('[', end='')
        print(answer,end='')
        print(']')

