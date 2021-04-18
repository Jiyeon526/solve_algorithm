import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()
P = "I" + "OI" * N

plen = len(P)
idx = 0
ans = 0
check = False

while idx <= M:
    if check:
        if S[idx:idx+2] == "OI":
            ans += 1
            idx = idx+2
        else:
            check = False
    else:
        if S[idx] == "I":
            if S[idx:idx+plen] == P:
                check = True
                ans += 1
                idx = idx + plen
            else:
                idx += 1
        else:
            idx += 1

print(ans)