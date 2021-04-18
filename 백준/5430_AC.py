import sys

input = sys.stdin.readline

Test_ = int(input())

while Test_ > 0:
    Test_ -= 1
    total_fun = input() # 수행해야되는 함수
    length = int(input()) # 문자열 길이

    if length == 0: # 만약에 빈 문자열이라면
        trash = input()
        if 'D' in total_fun: # D함수 실행시 error
            print('error')
        else: # R은 오류가 아닌 빈 배열 출력
            print('[]')
        continue

    lst = list(map(int, input().replace('[','').replace(']','').replace('\n','').split(',')))
    check = False
    check_rev = 0 # 뒤집었는지 확인
    for fun in total_fun:
        if len(lst) == 0 and fun == 'D': 
            print('error')
            check = True # 에러를 출력했는지 체크
            break 
        if fun == 'R':
            if check_rev == 0: # 뒤집었다면 체크
                check_rev = 1
            else:
                check_rev = 0
        elif fun == 'D':
            if check_rev == 1: # 뒤집은 상태라면 맨 뒤를 제거
                lst.pop()
            else: # 그게 아니라면 맨 앞을 제거
                lst.pop(0)
        
    if not check: # 에러를 출력하지 않았으면 밑을 출력한다.
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

