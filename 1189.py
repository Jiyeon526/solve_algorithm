import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

R, C, K = map(int, input().split())
M = [['0' for _ in range(C)] for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

for i in range(R):
    M[i] = list(map(str, input().strip()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def find(x, y, dist):
    global cnt

    if x == 0 and y == C-1:
        if dist == K:
            cnt += 1
        return
    elif dist > K:
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            if not visited[nx][ny] and M[nx][ny] != 'T':
                visited[nx][ny] = True
                find(nx, ny, dist+1)
                visited[nx][ny] = False

cnt = 0
visited[R-1][0] = True
find(R-1, 0, 1)
print(cnt)