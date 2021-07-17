import sys
from queue import PriorityQueue

def bfs():
    visit = [sys.maxsize] * 100001
    q = PriorityQueue()

    q.put([0, N])
    visit[N] = 0

    while q:
        now = q.get()

        if now[1] == K:
            return now[0]
        
        if 0<=now[1]-1<=100000 and visit[now[1]-1] > now[0] + 1:
            visit[now[1]-1] = now[0] + 1
            q.put([now[0] + 1, now[1]-1])

        if 0<=now[1]+1<=100000 and visit[now[1] + 1] > now[0] + 1:
            visit[now[1] + 1] = now[0] + 1
            q.put([now[0] + 1, now[1] + 1])

        if 0<=now[1]*2<=100000 and visit[now[1]*2] > now[0]:
            visit[now[1]*2] = now[0]
            q.put([now[0], now[1]*2])
    return -1

N, K = map(int, input().split())
print(bfs())