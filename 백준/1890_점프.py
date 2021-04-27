import sys
from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1: continue
        if board[i][j] == 0: continue

        d = board[i][j]
        

        if i+d<N:
            dp[i+d][j] += dp[i][j] # 아래
        if j+d<N:
            dp[i][j+d] += dp[i][j] # 오른쪽


print(dp[N-1][N-1])