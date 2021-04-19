import sys

N = int(input())
DP = [sys.maxsize] * (N+1)

DP[0] = DP[1] = 0
for i in range(2, N+1):
    tmp1 = tmp2 = tmp3 = sys.maxsize
    if i%3 == 0:
        tmp1 = DP[i//3] + 1
    if i%2 == 0:
        tmp2 = DP[i//2] + 1
    tmp3 = DP[i-1] + 1

    DP[i] = min(tmp1, tmp2, tmp3)

print(DP[N])