import sys

input = sys.stdin.readline

A, B = map(int, input().split())
m = int(input())
num_A = list(map(int, input().split()))
num_10 = 0
num_B = []

j = m-1
for i in range(m):
    num_10 += num_A[j] * A**i
    j -= 1

while num_10 > 0:
    num_B.append(num_10%B)
    num_10 //= B

num_B = num_B[::-1]
print(*num_B)
