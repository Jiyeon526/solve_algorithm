#어떻게 바꾸는데....
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = [[] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
qShark = deque() # 아기 상어 위치

for i in range(N):
    M[i] = list(map(int, input().split()))
    for j in range(N):
        if M[i][j] == 9:
            qShark.append((i, j)) # 상어 x, y좌표

SharkSize = 2 # 처음 상어 크기
fishCnt = 0 # 물고기 몇마리 먹었는지
while qShark: # 상어가 갈 수 있을때까지 
    SharkX, SharkY = qShark.popleft()
    qFish = deque()

    for i in range(N):
        for j in range(N):
            if M[i][j] < SharkSize and 1 <= M[i][j] <= 6: # 먹을 수 있는 물고기들 좌표 append
                qFish.append((i, j))

    smallDist = 1000000000 # 먹을 수 있는 물고기와 상어의 거리
    smallX = -1 # 최소 거리일때의 물고기 위치
    smallY = -1
   

    while qFish: # 먹을 수 있는 물고기 다 돌기
        qFishmove = deque() 
        FishX, FishY = qFish.pop() # 먹을 수 있는 물고기 좌표에서 상어 위치까지의 거리 구할려고
        qFishmove.append((FishX, FishY, 0))
        visit = [[False for _ in range(N)] for _ in range(N)]
        visit[FishX][FishY] = True
      
        while qFishmove: # 상어까지 갈 때 얼마나 걸리는지
            fishx, fishy, distf = qFishmove.popleft()

            if fishx == SharkX and fishy == SharkY: # 상어까지 갈 수 있다면
                if distf <= smallDist: # 거리 비교해서 더 작은 거리로 갈 수 있는 물고기 위치 넣어놈
                    smallDist = distf
                    smallX = FishX
                    smallY = FishY
                    # print("dist = ", distf, "x = ", smallX, "y = ", smallY)
                break
            
            for i in range(4):
                nx = fishx + dx[i]
                ny = fishy + dy[i]

                if 0 <= nx < N and 0 <= ny <N and (M[nx][ny] <= SharkSize or M[nx][ny] == 9) and not visit[nx][ny]:
                    visit[nx][ny] = True
                    qFishmove.append((nx, ny, distf+1))

    if smallX == -1 and smallY == -1: # 먹을 수 있는 물고기까지 가지 못함
        print(ans) 
        break
    else:
        fishCnt += 1 # 한마리 먹었으니깐
        ans += smallDist # 거리들의 합
        if fishCnt >= SharkSize: # 상어 크기 변경
            fishCnt -= SharkSize
            SharkSize += 1
        M[smallX][smallY] = 0 # 상어 위치 바꿔주고 qShark에 넣어주기
        qShark.append((smallX, smallY))
        


































# size = 1
# qFish = deque()

# while ?

# for i in range(N):
#     for j in range(N):
#         if M[i][j] == size:
#             qFish.append((i, j)) #물고기 좌표

# fishCnt = 0
# while qFish:

#     fishX, fishY = qFish.popleft()
#     visit = [[False for _ in range(N)] for _ in range(N)]
#     check = False # 아기상어가 물고기를 먹었는지 안먹었는지
#     X = 0, Y = 0, SSize = 0 # 아기상어 원래 위치 저장하는 변수
#     while qShark:

#         sharkX, sharkY, sharkSize, dist = qShark.popleft()

#         if dist == 0:
#             X = sharkX, Y = sharkY, SSize = sharkSize

#         visit[sharkX][sharkY] = True

#         if sharkX == fishX and sharkY == fishY:
#             ans += dist
#             fishCnt += 1
#             qShark.clear()
#             qShark.append((sharkX, sharkY, sharkSize, 0))
#             break
        
#         for i in range(4):
#             sharkNX = sharkX + dx[i]
#             sharkNX = sharkX + dy[i]

#             if 0 <= sharkNX < N and 0 <= sharkNX <N:
#                 if (not visit[sharkNX][sharkNY]) and M[sharkNX][sharkNY] <= sharkSize:
#                     qShark.append((sharkNX, sharkNY, sharkSize, dist+1))

#     if not check:
#         qShark.append((X, Y, SSize, 0))


    



