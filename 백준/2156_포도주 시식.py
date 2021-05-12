import sys

N = int(input())
wine = [0]

for i in range(N):
    wine.append(int(input()))

dp = [0]
dp.append(wine[1])
if N > 1: dp.append(wine[2]+dp[1])

for i in range(3, N+1):
    dp.append(max(dp[i-2] + wine[i], dp[i-1], dp[i-3]+wine[i-1]+wine[i]))

print(max(dp))