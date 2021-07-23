import sys


def perm(cnt):
    global ans

    if cnt == N:
        ans = max(sumArr(perm_arr), ans)
        return

    for i in range(N):
        if visit[i]:
            continue
        visit[i] = True
        perm_arr[cnt] = arr[i]
        perm(cnt+1)
        visit[i] = False


def sumArr(lst):
    res = 0

    for i in range(N-1):
        res += abs(lst[i] - lst[i+1])

    return res


N = int(input())
arr = list(map(int, input().split()))
ans = -800
visit = [False for _ in range(N)]
perm_arr = [-1] * N
perm(0)
print(ans)
