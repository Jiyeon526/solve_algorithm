import sys
from collections import deque

def D(N):
    return (N * 2) % 10000

def S(N):
    if N == 0:
        return 9999
    else:
        return N - 1

def L(N):
    th = N // 1000
    nums = N - (th * 1000)
    return (nums * 10) + th

def R(N):
    th = N % 10
    nums = N // 10
    return nums + (th * 1000)

def bfs(A, B):
    visit = [False for _ in range(10000)]
    q = deque()
    q.append([A, ""])
    visit[A] = True

    while q:
        size = len(q)

        for _ in range(size):
            now = q.popleft()
            if now[0] == B:
                print(now[1])
                return
            
            d = D(now[0])
            s = S(now[0])
            l = L(now[0])
            r = R(now[0])

            if not visit[d]:
                visit[d] = True
                q.append([d, now[1]+"D"])
            if not visit[s]:
                visit[s] = True
                q.append([s, now[1]+"S"])
            if not visit[l]:
                visit[l] = True
                q.append([l, now[1]+"L"])
            if not visit[r]:
                visit[r] = True
                q.append([r, now[1]+"R"])
    return

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    bfs(A, B)
