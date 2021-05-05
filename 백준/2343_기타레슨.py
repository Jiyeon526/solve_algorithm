import sys

N, M = map(int, input().split())
bluray = list(map(int, input().split()))

start = 1
end = sum(bluray)
ans = end
check = True

while start <= end:
    mid = (start + end) // 2

    cnt = 0
    size = 0
    for i in range(N):
        if bluray[i] > mid:
            check = False
            break
        
        size += bluray[i]
        if size >= mid:
            cnt += 1
            if size == mid:
                size = 0
            else:
                size = bluray[i]

    if size > 0: cnt += 1 
    if cnt <= M and check:
        ans = min(ans, mid)
        end = mid - 1
    else:
        start = mid + 1
        check = True

print(ans)