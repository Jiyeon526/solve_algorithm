import sys
sys.setrecursionlimit(10**9)

def dfs(n, std):
    global group
    visit[n] = True
    std.append(n)

    next = nums[n]
    if visit[next]:
        for i in range(len(std)):
            if std[i] == next:
                group += std[i:]
                break
        return
    else:
        dfs(next, std)

T = int(input())

for _ in range(T):
    N = int(input())
    nums = [0] + list(map(int, input().split()))
    visit = [False] * (N+1)
    group = []

    for i in range(1, N+1):
        if not visit[i]:
            dfs(i, [])

    print(N - len(group))
    

