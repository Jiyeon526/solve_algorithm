import sys

treeCnt, needTree = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)
ans = 0
while start<=end:
    mid = (start + end) // 2

    cut = 0
    for t in tree:
        if t-mid > 0: cut += t-mid
        if needTree <= cut: break

    if cut >= needTree:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)