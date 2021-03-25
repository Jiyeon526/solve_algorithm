import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())
bus = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, w = map(int, input().split())
    bus[a].append((b, w))

S, E = map(int, input().split())

hq = []
G = [1000000000 for _ in range(N+1)]
G[S] = 0
heapq.heappush(hq, (G[S], S))

while hq:
    weight, now = heapq.heappop(hq)
    
    if now == E:
        print(G[E])
        break

    for nv, nw in bus[now]:
        if G[nv] > nw + weight:
            G[nv] = nw + weight
            heapq.heappush(hq, (G[nv], nv))
 

