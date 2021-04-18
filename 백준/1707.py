# 중복 제거를 안해서 틀린듯..?
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    V, E = map(int, input().split())
    num_lst = [[] for _ in range(V+1)] # 연결되있는것들
    num = [[0, 0] for _ in range(E)] # 노드들
    graph = [0 for _ in range(V+1)] # 2개로 나눠지는지 확인(1, 2로 나눔)
    check = True

    for i in range(E):
        n1, n2 = map(int, input().split())
        
        m = max(n1, n2)
        n = min(n1, n2)
        num[i][0] = n
        num[i][1] = m

        num_lst[n1].append(n2)
        num_lst[n2].append(n1)

    num.sort()
    for i in range(E):
        n1 = num[i][0]
        n2 = num[i][1]

        # 만약에 n1보다 작은 값들이 이미 있다면
        for n in num_lst[n1]:
            if n < n1:
                if graph[n] > 0: # 근데 그 값이 연결되있다면
                    graph[n1] = graph[n]%2 + 1 # n1의 값은 n의 반대 

        for n in num_lst[n2]:
            if n < n2:
                if graph[n] > 0:
                    graph[n2] = graph[n]%2 + 1

        if graph[n1] > 0:
            if graph[n2] > 0:
                if graph[n1] == graph[n2]: # 만약 둘 다 값이 있는데 둘의 값이 같다면 노노
                    check = False
            if graph[n2] == 0: 
                graph[n2] = graph[n1]%2 + 1
        else:
            if graph[n2] > 0:
                graph[n1] = graph[n2]%2 + 1
            else: # 이 모든게 다 통과하고 오면...
                graph[n1] = 1
                graph[n2] = 2
    
    if check:
        print('YES')
    else:
        print('NO')

