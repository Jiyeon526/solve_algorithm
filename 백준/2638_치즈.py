import sys
from collections import deque

N, M = map(int, input().split())
board = [[-1 for _ in range(M)] for _ in range(N)]
cheese = deque()

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j] == 0:
            board[i][j] = -1
        else:
            board[i][j] = tmp[j]
            cheese.append([i, j])
print("board")
for i in range(N):
    print(*board[i])

# 외부 내부 나누기
q = deque()
visit = [[False for _ in range(M)] for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q.append([0, 0])
visit[0][0] = True
board[0][0] = 2

while q:
    now = q.popleft()

    for i in range(4):
        nx = now[0] + dx[i]
        ny = now[1] + dy[i]

        if 0<=nx<N and 0<=ny<M:
            if not visit[nx][ny] and board[nx][ny] == -1:
                q.append([nx, ny])
                visit[nx][ny]
                board[nx][ny] = 2 # 외부 공기

print("board 나눔")
for i in range(N):
    print(*board[i])

time = 0
while True:
    melt = deque()
    print("cheese = ", cheese)
    cheese_size = len(cheese)
    for _ in range(cheese_size):
        # print("now ", now)
        now = cheese.popleft()
        cnt = 0

        for i in range(4):
            
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            # print("next ", nx, " ", ny)

            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny] == 2:
                    cnt += 1
        # print(cnt)
        if cnt < 2:
            cheese.append(now)
        else:
            melt.append(now)

    print("melt = ", melt)
    melt_size = len(melt)
    for _ in range(melt_size):
        now = melt.popleft()

        board[now[0]][now[1]] = -1
        melt.append(now)

    visit = [[False for _ in range(M)] for _ in range(N)]
    while melt:
        now = melt.popleft()
        visit[now[0]][now[1]] = True

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if 0<=nx<N and 0<=ny<M:
                if not visit[nx][ny] and board[nx][ny] == -1:
                    melt.append([nx, ny])
                    visit[nx][ny]
                    board[nx][ny] = 2
    time += 1

    if len(cheese) == 0:
        break

print(time)

