import sys

N = int(input())
card = list(map(int, input().split()))
card.insert(0, 0)
dp = [0] * (N+1)

for i in range(1, N+1):
    for j in range(i, N+1):
        dp[j] = max(dp[j], card[i] + dp[j-i])

print(dp[N])
