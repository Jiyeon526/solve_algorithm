import sys
from collections import deque

def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    nightdx = [-1, -2, 1, 2, -1, -2, 1, 2]
    nightdy = [2, 1, 2, 1, -2, -1, -2, -1]
    visit = [[[False for _ in range(K+1)] for _ in range(W)] for _ in range(H)]
    q = deque()
    q.append([0, 0, 0, 0])
    visit[0][0][0] = True

    while q:
        size = len(q)

        for _ in range(size):
            now = q.popleft()

            if now[0] == H - 1 and now[1] == W - 1:
                print(now[3])
                return
            
            for d in range(4):
                nx = now[0] + dx[d]
                ny = now[1] + dy[d]

                if 0<=nx<H and 0<=ny<W and not visit[nx][ny][now[2]] and board[nx][ny] != 1:
                    visit[nx][ny][now[2]] = True
                    q.append([nx, ny, now[2], now[3] + 1])
            
            for d in range(8):
                nx = now[0] + nightdx[d]
                ny = now[1] + nightdy[d]

                if 0<=nx<H and 0<=ny<W and now[2] < K and not visit[nx][ny][now[2] + 1] and board[nx][ny] != 1:
                    visit[nx][ny][now[2] + 1] = True
                    q.append([nx, ny, now[2] + 1, now[3] + 1])
    print(-1)
    return 


K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
bfs()
