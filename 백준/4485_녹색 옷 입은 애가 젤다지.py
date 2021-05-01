import sys
import heapq

input = sys.stdin.readline

tc = 1
while True:
    N = int(input())
    
    if N == 0:
        break
    
    board = [[] for _ in range(N)]
    for i in range(N):
        board[i] = list(map(int, input().split()))
    
    rupee = [[100000000 for _ in range(N)] for _ in range(N)]
    rupee[0][0] = board[0][0] # 처음 시작값 저장하기
    
    hq = []
    heapq.heappush(hq, (rupee[0][0], 0, 0))

    ans = 100000000000000 # 답
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while hq:
        R, X, Y = heapq.heappop(hq)

        if X == N-1 and Y == N-1:
            ans = min(ans, R)

        for i in range(4): # 상하좌우 이동
            nx = X + dx[i]
            ny = Y + dy[i]

            if 0<=nx<=N-1 and 0<=ny<=N-1:
                if rupee[nx][ny] > R + board[nx][ny]: # 만약 루피값이 이때까지 이동한 값 + 해당 위치의 루피값보다 크다면
                    rupee[nx][ny] = R + board[nx][ny] # 루피값갱신
                    heapq.heappush(hq, (rupee[nx][ny], nx, ny))

    S = "Problem " + str(tc) + ": " + str(ans)
    print(S)
    tc += 1
