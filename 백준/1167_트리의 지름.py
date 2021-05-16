import sys
from collections import deque

V = int(input())
tree = {}

for _ in range(V):
    tmp = list(map(int, input().split()))
    for i in range(1, len(tmp)-1, 2):
        tree.setdefault(tmp[0], []).append((tmp[i], tmp[i+1]))

def bfs(start):
    q = deque()
    q.append((start, 0))
    visit = [False] * (V+1)
    visit[start] = True

    result = [0, 0]
    while q:
        now, weight = q.popleft()
        for node in tree[now]:
            next, w = node[0], node[1]
            if not visit[next]:
                visit[next] = True
                q.append((next, w + weight))
                
                if result[1] < w + weight:
                    result[1] = w + weight
                    result[0] = next
    
    return result

first = bfs(1)
ans = bfs(first[0])
print(ans[1])
