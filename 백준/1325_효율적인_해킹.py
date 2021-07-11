import sys
sys.setrecursionlimit(10**9)

def dfs(n):
    check[n] = 1
    if n in com:
        for c in com[n]:
            if check[c] == 0:
                check[c] = 1
                dfs(c)

N, M = map(int, input().split())
com = {}

for _ in range(M):
    A, B = map(int, input().split())
    if B not in com:
        com[B] = []
    com[B].append(A)

visit = [False] * (N+1)
cnt = [0] * (N+1)
for i in range(1, N+1):
    check = [0] * (N+1)
    dfs(i)
    cnt[i] = sum(check)

max_com = max(cnt)
answer = []
for i in range(1, N+1):
    if cnt[i] == max_com:
        answer.append(str(i))
print(" ".join(answer))