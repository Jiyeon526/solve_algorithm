import sys

N, C = map(int, input().split())
H = []

for _ in range(N):
    H.append(int(input()))

H.sort()
start = 0
end = H[N-1] - H[0]
ans = 0
while start <= end:
    mid = (start + end) // 2

    cnt = 1
    s = H[0]
    for i in range(1, N):
        if H[i] - s >= mid:
            s = H[i]
            cnt += 1
        # if cnt == C:
        #     break

    if cnt >= C:
        ans = max(mid, ans)
        start = mid + 1
    else:
        end = mid - 1

print(ans) 


