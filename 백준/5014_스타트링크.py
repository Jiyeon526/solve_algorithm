import sys
from collections import deque

def stair():
    q = deque()
    q.append(S)
    visit = [False for _ in range(F+1)]
    button = 0

    while q:
        size = len(q)
        
        for _ in range(size):
            now = q.popleft()

            if now == G:
                return button

            up = now + U
            down = now - D

            if 1<=up<=F and not visit[up]:
                visit[up] = True
                q.append(up)
                
            if 1<=down<=F and not visit[down]:
                visit[down] = True
                q.append(down)

        button += 1
    
    return -1

F, S, G, U, D = map(int, input().split())
ans = stair()
if ans == -1:
    print("use the stairs")
else:
    print(ans)
