import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, cnt):
    if cnt == n*n:
        return

    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    for k in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n:
            if board[nx][ny] < board[x][y]:
                dp[x][y] += dfs(nx, ny, cnt+1)
    
    return dp[x][y]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        dfs(i, j, 0)

for i in range(n):
    print(*dp[i])