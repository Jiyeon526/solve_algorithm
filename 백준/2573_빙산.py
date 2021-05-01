import sys
from collections import deque
import copy

N, M = map(int, input().split())
board = [[] for _ in range(N)]
qIce = deque() # 빙산의 위치

for i in range(N):
    board[i] = list(map(int, input().split()))
    for j in range(M):
        if board[i][j] != 0:
            qIce.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y, cnt): # 영역이 둘로 나눠지는 확인하기 위해
    q = deque()
    q.append((x, y))

    while q:
        X, Y = q.popleft()

        for i in range(4):
            nx = X + dx[i]
            ny = Y + dy[i]

            if 0<=nx<N and 0<=ny<M:
                if visit[nx][ny] == 0 and board[nx][ny] != 0:
                    visit[nx][ny] = cnt
                    q.append((nx, ny)) 

time = 0
while qIce:
    # 영역 확인
    qIce_clone = qIce.copy()
    visit = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 1
    iceSize = len(qIce_clone)

    for S in range(iceSize):
        i, j = qIce_clone.popleft()
        if visit[i][j] == 0:
            bfs(i, j, cnt)
            cnt += 1

    if cnt != 2: # 만약에 영역이 둘 이상으로 나눠지면 그만
        break
    
    size = len(qIce) # 빙산 수 만큼 돌기
    board_clone = copy.deepcopy(board)
    for s in range(size): # 빙산 - 물 하는거
        IceX, IceY = qIce.popleft()
        waterCnt = 0
        for i in range(4):
            nIx = IceX + dx[i]
            nIy = IceY + dy[i]

            if 0<=nIx<N and 0<=nIy<M:
                if board[nIx][nIy] == 0:
                    waterCnt += 1
        
        board_clone[IceX][IceY] -= waterCnt
        if board_clone[IceX][IceY] <= 0: 
            board_clone[IceX][IceY] = 0
        else:
            qIce.append((IceX, IceY)) # 빙산이 안사라지면 다시 넣어주기
    
    board = copy.deepcopy(board_clone)
    time += 1

if len(qIce) == 0: # 다 녹으면
    print(0)
else:
    print(time)
    

    

    