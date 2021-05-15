import sys
sys.setrecursionlimit(10**9)

def fun(now):
    if now == N: return

    for i in range(now):
        if A[now] > A[i]:
            dp[now] = max(dp[now], dp[i]+1)
    
    fun(now+1)

N = int(input())
A = list(map(int, input().split()))
dp = [1] * N
fun(0)

# for i in range(N):
#     for j in range(i):
#         if A[i] > A[j]:
#             dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))