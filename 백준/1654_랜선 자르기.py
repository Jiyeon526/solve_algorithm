import sys

K, N = map(int, input().split())
line = [int(input()) for _ in range(K)]

start = 1
end = 3000000000
ans = 0
while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for i in range(K):
        cnt += line[i]//mid

    if cnt >= N:
        start = mid + 1
        ans = max(ans, mid)
    else:
        end = mid - 1
print(ans)