import sys

input = sys.stdin.readline

def path(L, board):
    tmp = [0 for _ in range(k)]

    for i in range(k): # 처음 시작 점
        current = i
        for j in range(L):
            if board[current][j] == 1:
                current -= 1
            elif board[current][j] == 2:
                current += 1
        tmp[current] = i
    
    return tmp

    
k = int(input())
n = int(input())
top = [[0 for _ in range(n)] for _ in range(k)]
bottom = [[0 for _ in range(n)] for _ in range(k)]

result = [ 0 for _ in range(k)]
s = list(input().strip())

for i in range(k):
    result[i] = ord(s[i]) - ord('A')

idx = 0
for i in range(n):
    s = list(input().strip())
    if '?' in s:
        idx = i
        break
    for j in range(k-1):
        if s[j] == '-':
            top[j][i] = 2 # 세로 j 가로 i
            top[j+1][i] = 1

for j in range(n-idx-1):
    s = list(input().strip())
    for t in range(k-1):
        if s[t] == '-':
            bottom[t][j] = 2
            bottom[t+1][j] = 1

top_result = path(idx, top)
bottom_result = path(n-idx-1, bottom)
bottom_r = [0 for _ in range(k)]

for i in range(k):
    bottom_r[bottom_result[i]] = i

ans = ['x' for _ in range(k-1)]
for i in range(k-1):
    if top_result[i] == result[bottom_r[i+1]] and top_result[i+1] == result[bottom_r[i]]:
        ans[i] = "-"
    else:
        ans[i] = "*"

for i in range(k-1):
    if ans[i] == '-':
        top_result[i], top_result[i+1] = top_result[i+1], top_result[i]

check = True
for i in range(k-1):
    if not (top_result[i] == result[bottom_r[i]] and top_result[i+1] == result[bottom_r[i+1]]):
        check = False

if check:
    print(''.join(ans))
else:
    print('x'*(k-1))

