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
    rupee[0][0] = board[0][0]
    
    hq = []
    heapq.heappush(hq, (rupee[0][0], 0, 0))

    visit = [[False for _ in range(N)] for _ in range(N)]
    # visit[0][0] = True

    ans = 100000000000000
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while hq:
        R, X, Y = heapq.heappop(hq)

        if X == N-1 and Y == N-1:
            ans = min(ans, R)

        for i in range(4):
            nx = X + dx[i]
            ny = Y + dy[i]

            # if 0<=nx<=N-1 and 0<=ny<=N-1 and not visit[nx][ny]:
            if 0<=nx<=N-1 and 0<=ny<=N-1:
                if rupee[nx][ny] > R + board[nx][ny]:
                    rupee[nx][ny] = R + board[nx][ny]
                    # visit[nx][ny] = True
                    heapq.heappush(hq, (rupee[nx][ny], nx, ny))

    S = "Problem " + str(tc) + ": " + str(ans)
    print(S)
    tc += 1
