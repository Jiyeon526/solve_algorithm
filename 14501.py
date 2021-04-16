import sys

N = int(input())
T = [0] * N
P = [0] * N

for i in range(N):
    T[i], P[i] = map(int, input().split())

money = [0] * (N+1)
for i in range(N-1,-1,-1):
    if i + T[i] > N:
        money[i] = money[i+1]
    else:
        money[i] = max(money[i+1], P[i] + money[i+T[i]])

print(max(money))