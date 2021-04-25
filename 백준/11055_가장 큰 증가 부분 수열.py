import sys

N = int(input())
A = list(map(int, input().split()))
dp = [0] * N
dp[0] = A[0]

for i in range(1, N):
    dp[i] = A[i]
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+A[i])

# print(dp)
print(max(dp))
