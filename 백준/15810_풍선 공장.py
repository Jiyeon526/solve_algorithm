import sys

N, M = map(int, input().split())
A = list(map(int, input().split()))

# if M == 0:
#     print(0)
#     exit(0)

# A.sort()
# if N >= M:
#     print(A[M-1])
#     exit(0)

start = 0; end = max(A)*M # 풍선이 다 만들어지는 시간
ans = end
while start <= end:
    mid = (start + end) // 2

    people = 0 # 해당 시간에 몇 명 불어줄 수 있는지
    for i in range(N):
        people += (mid//A[i])
        if people >= M: break

    if people >= M:
        ans = min(ans, mid)
        end = mid - 1
    else:
        start = mid + 1
print(ans)