import sys
from collections import deque

def bfs(s, e, c):
    q = deque()
    visit[s][e] = True
    board[s][e] = c
    q.append([s, e])

    while q:
        now = q.popleft()

        for d in range(4):
            nx = now[0] + dx[d]
            ny = now[1] + dy[d]

            if 0<=nx<N and 0<=ny<N and not visit[nx][ny] and board[nx][ny] == 1:
                visit[nx][ny] = True
                board[nx][ny] = c
                q.append([nx, ny])
    return

def connect(s, e):
    q = deque()
    cVisit = [[False for _ in range(N)] for _ in range(N)]
    q.append([s, e])
    cVisit[s][e] = True
    res = 0

    while q:
        size = len(q)
        
        for _ in range(size):
            now = q.popleft()

            if board[now[0]][now[1]] != 0 and board[now[0]][now[1]] != board[s][e]:
                return res

            for d in range(4):
                nx = now[0] + dx[d]
                ny = now[1] + dy[d]

                if 0<=nx<N and 0<=ny<N and not cVisit[nx][ny] and board[nx][ny] != board[s][e]:
                    cVisit[nx][ny] = True
                    q.append([nx, ny])
        res += 1
    
    return -1

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visit = [[False for _ in range(N)] for _ in range(N)]
cnt = 2

for i in range(N):
    for j in range(N):
        if not visit[i][j] and board[i][j] == 1:
            bfs(i, j, cnt)
            cnt += 1

ans = sys.maxsize
for i in range(N):
    for j in range(N):
        if board[i][j] > 0:
            tmp = connect(i, j)
            if tmp != -1:
                ans = min(ans, tmp)

print(ans-1)