import sys
from collections import deque

def bfs(s, e):
    q = deque()
    visit = [[False for _ in range(M)] for _ in range(N)]
    q.append([s, e])
    visit[s][e] = True
    board[s][e] = 2

    while q:
        now = q.popleft()

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if 0<=nx<N and 0<=ny<M and not visit[nx][ny] and board[nx][ny] == 0:
                q.append([nx, ny])
                board[nx][ny] = 2
                visit[nx][ny] = True


N, M = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
board = [[0 for _ in range(M)] for _ in range(N)]
Cheese = deque()
remove = deque()

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        board[i][j] = tmp[j]
        if board[i][j] == 1:
            Cheese.append([i, j])
bfs(0, 0)

time = 0
CheeseSize = 0
while True:
    size = len(Cheese)

    if size == 0:
        print(time)
        print(CheeseSize)
        break

    for _ in range(size):  # 공기 중 치즈 확인
        nowCheese = Cheese.popleft()
        flag = True

        for d in range(4):
            ncx = nowCheese[0] + dx[d]
            ncy = nowCheese[1] + dy[d]

            if 0<=ncx<N and 0<=ncy<M and board[ncx][ncy] == 2:
                remove.append(nowCheese)
                flag = False
                break
        
        if flag:
            Cheese.append(nowCheese)
    
    CheeseSize = len(remove)
    while remove:
        nowRemove = remove.popleft()
        bfs(nowRemove[0], nowRemove[1])
    
    time += 1


