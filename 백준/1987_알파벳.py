import sys

ans = 0
def find(x, y, cnt):
    global ans
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    if ans < cnt:
        ans = cnt
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= R or ny < 0 or ny >= C: continue
        if alp[board[nx][ny]] == 1: continue

        alp[board[nx][ny]] = 1
        find(nx, ny, cnt+1)
        alp[board[nx][ny]] = 0
    
    return

R, C = map(int, input().split())
board = [[-1 for _ in range(C)] for _ in range(R)]
alp = [0] * 26

for i in range(R):
    tmp = input()
    for j in range(C):
        board[i][j] = ord(tmp[j]) - 65

alp[board[0][0]] = 1
find(0, 0, 1)
print(ans)