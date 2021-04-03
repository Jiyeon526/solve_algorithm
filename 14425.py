import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = {}

for _ in range(N):
    key = input().strip()
    if S.get(key) == None:
        S[key] = 0

# print(S)

for _ in range(M):
    key = input().strip()
    if S.get(key) == None:
        continue
    else:
        S[key] += 1

print(sum(S.values()))
