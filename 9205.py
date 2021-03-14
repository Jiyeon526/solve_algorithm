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
    location = [[0,0] for _ in range(shop_num+2)]
    visited = [False for _ in range(shop_num+2)]
    connect = [[] for _ in range(shop_num+2)]

    for i in range(shop_num+2):
        x, y = map(int, input().split())
        location[i][0] = x
        location[i][1] = y
    
    for i in range(shop_num+2):
        for j in range(shop_num+2):
            if i == j:
                continue
            if(abs(location[i][0] - location[j][0]) + abs(location[i][1] - location[j][1])) <= 1000:
                connect[i].append(j)
    visited[0] = True
    find(0)

















    # shop_num = int(input())
    # home_x, home_y = map(int, input().split())

    # shop = [[0, 0] for _ in range(shop_num)]
    # for i in range(shop_num):
    #     x, y = map(int, input().split())
    #     shop[i][0] = x
    #     shop[i][1] = y

    # festival_x, festival_y = map(int, input().split())
    
    # visited = [False for _ in range(shop_num)]
    # q = deque()
    # q.append((home_x, home_y))
    # check = False
    # while q:
    #     print(q)
    #     x, y = q.popleft()
    #     if (abs(x - festival_x) + abs(y - festival_y)) <= 1000:
    #         check = True
    #         print("happy")
    #     elif False not in visited: #편의점 다 갔는데도 페스티벌 못감
    #         check = True
    #         print("sad")
    #     else:
    #         for i in range(shop_num):
    #             if not visited[i] and (abs(x - shop[i][0]) + abs(y - shop[i][1])) <= 1000:
    #                 visited[i] = True
    #                 q.append((shop[i][0], shop[i][1]))

    # if not check: # 맥주 다 마셔서 못감
    #     print("sad")




