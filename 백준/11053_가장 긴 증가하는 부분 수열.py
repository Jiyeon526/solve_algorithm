import sys

N = int(input())
A = list(map(int, input().split()))
dp = [0] * N
dp[0] = 1

for i in range(1, N):
    tmp = 1
    for j in range(i):
        if A[j] < A[i]:
            tmp = max(tmp, dp[j]+1)
    dp[i] = tmp

# print(dp)
print(max(dp))