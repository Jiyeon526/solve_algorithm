import sys
sys.setrecursionlimit(10**9)

def find(a):
    if uf[a]==a: return a
    uf[a] = find(uf[a])
    return uf[a]

def union(a, b):
    aa = find(a)
    bb = find(b)
    if aa > bb: uf[a] = bb
    else: uf[b] = aa

n, m = map(int, input().split())
uf = [i for i in range(n)]

cycle = False
ans = 1
for i in range(m):
    a, b = map(int, input().split())

    if find(a) == find(b):
        cycle = True
        ans = i + 1
        break
    else:
        union(uf[a], uf[b])

if cycle:
    print(ans)
else:       
    print(0)