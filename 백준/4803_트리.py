import sys
sys.setrecursionlimit(10**9)

def find(x):
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return -1
    
    if level[x] > level[y]:
        parent[y] = x
        level[x] += level[y]
    else:
        parent[x] = y
        level[y] += level[x]
    return 0

case = 0
while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break
    
    case += 1
    parent = [i for i in range(n+1)]
    level = [1 for _ in range(n+1)]
    
    flag = False # 사이클인지아닌지
    for i in range(m):
        v, w = map(int, input().split())
        if union(v, w) == -1:
            flag = True
    
    cnt = 0
    for i in range(1, n+1):
        if i == parent[i]:
            cnt += 1
    
    ans = "Case " + str(case) + ": " 
    if cnt == 0 or flag:
        ans += "No trees."
    elif cnt == 1:
        ans += "There is one tree."
    else:
        ans += "A forest of " + str(cnt) + " trees."
    print(ans)
