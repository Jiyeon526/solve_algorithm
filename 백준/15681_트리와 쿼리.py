import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def subTree(n):
    cnt[n] = 1
    for i in tree[n]:
        if cnt[i] == 0:
            subTree(i)
            cnt[n] += cnt[i]
    return

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N+1)]
cnt = [0 for _ in range(N+1)]

for i in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

subTree(R)

for i in range(Q):
    u = int(input())
    print(cnt[u])