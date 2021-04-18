import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
variable = [[0 for _ in range(2)] for _ in range(M)]
boolean = [True for _ in range(N+1)]

for i in range(M):
    variable[i] = list(map(int, input().split()))

def fun(cnt):
    for i in range(M):
        if abs(variable[i][0]) > cnt or abs(variable[i][1]) > cnt:
            continue
        
        x1 = -1 if variable[i][0] < 0 else 1
        x2 = -1 if variable[i][1] < 0 else 1
        x1_b = boolean[abs(variable[i][0])]
        x2_b = boolean[abs(variable[i][1])]
        if x1 == -1: x1_b = False if x1_b else True
        if x2 == -1: x2_b = False if x2_b else True

        ans = x1_b or x2_b
        if not ans:
            return False

    return True

def perm(cnt):
    global check

    if check:
        return

    if cnt == N+1:
        if fun(cnt):
            print(1)
            check = True
        return
    elif cnt >= 2:
        if not fun(cnt):
            return
    
    boolean[cnt] = True
    perm(cnt+1)
    
    boolean[cnt] = False
    perm(cnt+1)   

check = False
perm(1)
if not check:
    print(0)