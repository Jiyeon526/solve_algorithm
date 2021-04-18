import sys

input = sys.stdin.readline

n, m = map(int, input().split())
edge = []
for _ in range(m):
    edge.append(tuple(map(int, input().split())))

MAX_TIME = sys.maxsize
time = [MAX_TIME for _ in range(n+1)]
time[1] = 0

def bellman(start):
    for i in range(n-1):
        for j in range(m):
            s, e, t = edge[j]
            if time[s] != MAX_TIME and time[e] > time[s] + t:
                time[e] = time[s] + t

    for j in range(m):
        s, e, t = edge[j]
        if time[s] != MAX_TIME and time[e] > time[s] + t:
            return True

    return False

negativeCycle = bellman(1)

if negativeCycle: print(-1)
else :
    ans = []
    for i in range(2, n+1):
        if time[i] == MAX_TIME:
            ans.append("-1")
        else:
            ans.append(str(time[i]))
    print("\n".join(ans))