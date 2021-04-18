import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
M = [[] for _ in range(R)]

for i in range(R):
    M[i] = list(map(str, input().strip()))

# 시작점 찾기
qw = deque()
q = deque()
visited = [[False for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        if(M[i][j] == 'S'):
            q.append((i, j, 0))
            visited[i][j] = True
        if(M[i][j] == '*'):
            qw.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
check = False

while q:
    if check:
        break

    lenWater = len(qw)
    for _ in range(lenWater):
        wx, wy = qw.popleft()
        # print(wx, wy)
        for i in range(4):
            nwx = wx + dx[i]
            nwy = wy + dy[i]

            if(0 <= nwx < R and 0 <= nwy < C):
                if(M[nwx][nwy] == '.' and not visited[nwx][nwy]):
                    qw.append((nwx, nwy))
                    visited[nwx][nwy] = True

    # print("q = ", q)

    lenS = len(q)
    # print("q= ", q)
    for _ in range(lenS):
        x, y, cnt = q.popleft()

        if(M[x][y] == 'D'):
            print(cnt)
            check = True
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(0 <= nx < R and 0 <= ny < C):
                if((M[nx][ny] == '.' or M[nx][ny] == 'D') and not visited[nx][ny]):
                    q.append((nx, ny, cnt+1))
                    visited[nx][ny] = True

if not check:
    print('KAKTUS')
