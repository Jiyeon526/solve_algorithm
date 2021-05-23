import sys
import heapq

def mst():
    q = []
    heapq.heappush(q, [0, 1])
    visit = [False] * (V+1)
    result = 0

    while q:
        dis, node = heapq.heappop(q)
        if visit[node]:
            continue

        result += dis
        visit[node] = True
        for a, c in edge[node]:
            if not visit[a]:
                heapq.heappush(q, [c, a])
    
    return result


V, E = map(int, input().split())
edge = [[] for _ in range(V+1)]

for _ in range(E):
    A, B, C = map(int, input().split())
    edge[A].append([B, C])
    edge[B].append([A, C])

print(mst())