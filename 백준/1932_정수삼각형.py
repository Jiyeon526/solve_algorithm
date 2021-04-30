import sys

N = int(input())
num = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(len(num[i]))] for i in range(N)]
dp[0][0] = num[0][0]

for i in range(N-1):
    for j in range(len(num[i+1])-1):
        if dp[i+1][j] != 0:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]+num[i+1][j])
        else:
            dp[i+1][j] = dp[i][j]+num[i+1][j]
        dp[i+1][j+1] = dp[i][j]+num[i+1][j+1]

print(max(dp[N-1]))