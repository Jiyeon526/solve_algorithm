import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(n):
    dp[n][0] = 1 # 내가 얼리어답터
    dp[n][1] = 0
    visit[n] = True

    for i in tree[n]:
        if not visit[i]:
            dfs(i)
            dp[n][0] += min(dp[i][0], dp[i][1]) # 자식도 얼리가나 아닐수있음
            dp[n][1] += dp[i][0] # 내가 얼리아니면 무조건 자식은 얼리

N = int(input())
tree = [[] for _ in range(N+1)]
dp = [[0, 0] for _ in range(N+1)]
visit = [False] * (N+1)

for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dfs(1)
print(min(dp[1][0], dp[1][1]))