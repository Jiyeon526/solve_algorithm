import sys

# 0과 1 불린 횟수 저장
zero = [0] * 41
one = [0] * 41

zero[0] = 1
zero[1] = 0
one[0] = 0
one[1] = 1

for i in range(2, 41):
    zero[i] = zero[i-1] + zero[i-2]
    one[i] = one[i-1] + one[i-2]

TC = int(input())
while TC > 0:
    TC -= 1
    n = int(input())
    print(zero[n], one[n])