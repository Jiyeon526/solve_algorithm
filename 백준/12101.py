import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, k = map(int, input().split())

def sum_123(s, lst):
    global cnt
    global stop

    if stop:
        return

    if s == n:
        if cnt == k:
            print("+".join(map(str, lst)))
            stop = True
        cnt += 1
        return
    elif s > n:
        return
    
    for i in range(1, 4):
        lst.append(i)
        sum_123(s+i, lst)
        lst.pop()


lst = []
cnt = 1
stop = False
sum_123(0, lst)

if not stop:
    print(-1)

#와.... 문제 제대로 안읽었네...뭐했냐.....