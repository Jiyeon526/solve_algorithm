import sys
import math
import heapq

def mst():
    visit = [False] * (N+1)
    result = 0
    q = []
    heapq.heappush(q, [0, 1])
    while q:
        dis, node = heapq.heappop(q)
        if visit[node]:
            continue

        result += dis
        visit[node] = True

        for i in range(1, N+1):
            if visit[i]: continue
            heapq.heappush(q, [adj[node][i], i])

    return result

N, M = map(int, input().split())
space = [[] for _ in range(N+1)]
adj = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    x, y = map(int, input().split())
    space[i].append(x)
    space[i].append(y)

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j: continue
        dis = math.sqrt((space[i][0] - space[j][0])**2 + (space[i][1] - space[j][1])**2)
        adj[i][j] = adj[j][i] = dis

for _ in range(M):
    a, b = map(int, input().split())
    adj[a][b] = adj[b][a] = 0

# for i in range(N+1):
#     print(*(adj[i]))

print('{0:0.2f}'.format(mst()))