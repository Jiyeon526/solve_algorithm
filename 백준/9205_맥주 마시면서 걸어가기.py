import sys
from queue import deque

test_case = int(input())

def find(start):
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        if (shop_num + 1) in connect[now]:
            print("happy")
            return
        for i in connect[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    
    print("sad")
    return
            

for _ in range(test_case):
    shop_num = int(input())
    location = [[0,0] for _ in range(shop_num+2)] # 각 곳의 장소 위치 x, y 저장
    visited = [False for _ in range(shop_num+2)] # 그곳에 방문했는지 안했는지 체크
    connect = [[] for _ in range(shop_num+2)] # 서로 연결되어있는지 체크

    for i in range(shop_num+2):
        x, y = map(int, input().split())
        location[i][0] = x
        location[i][1] = y
    
    # 두 곳을 비교해서 둘의 거리가 1000이하라면 연결됨을 표시
    for i in range(shop_num+2):
        for j in range(shop_num+2):
            if i == j:
                continue
            if(abs(location[i][0] - location[j][0]) + abs(location[i][1] - location[j][1])) <= 1000:
                connect[i].append(j) # i에서 j로 갈 수 있다.
    visited[0] = True
    find(0)
