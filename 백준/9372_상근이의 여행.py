import sys
from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = {}

    for _ in range(M):
        a, b = map(int, input().split())
        A.setdefault(a, []).append(b)
        A.setdefault(b, []).append(a)

    visit = [False]*N ; visit[0] = True
    q = deque(); q.append(1)
    cnt = 0
    while q:
        now = q.popleft()
        
        if A.get(now):
            for v in A[now]:
                if not visit[v-1]:
                    cnt += 1
                    visit[v-1] = True
                    q.append(v)
    print(cnt)