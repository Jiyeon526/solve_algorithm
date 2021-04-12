import sys

input = sys.stdin.readline

S = input()
N = int(input())
A = []
for i in range(N):
    A[i] = input()

slen = len(S)
for i in range(slen):
    for