import sys


def powerSet(idx, s, lst):
    global ans

    if idx >= N:
        if s == S and len(lst) != 0:
            ans += 1
        return

    s += arr[idx]
    lst.append(arr[idx])
    powerSet(idx+1, s, lst)

    s -= arr[idx]
    lst.pop()
    powerSet(idx+1, s, lst)


N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
powerSet(0, 0, [])
print(ans)
