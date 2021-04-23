import sys

n = int(input())
A = list(map(int, input().split()))
dp = [0] * n
dp[0] = A[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + A[i], A[i], A[i-1]+A[i])

# print(dp)
print(max(dp))