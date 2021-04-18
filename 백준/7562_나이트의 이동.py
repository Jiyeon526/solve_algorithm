import sys
from collections import deque

input = sys.stdin.readline

# 테스트 케이스 입력
Test_case = int(input())

# 테스트 케이스 만큼 반복
while Test_case > 0:
    #체스판 크기 입력
    L = int(input())

    # 나이트의 처음 위치와 마지막 위치 입력
    first_night_x, first_night_y = map(int, input().split())
    finally_night_x, finally_night_y = map(int, input().split())

    # 그 위치에 방문했는지 체크하는 list
    visited = [[False]*L for _ in range(L)]
    # 최소 이동거리를 기록할 list
    board = [[0]*L for _ in range(L)]
    # 나이트가 이동할 수 있는 방향 list
    dx = [-2, 2, -1, 1]
    dy = [-1, 1, -2, 2]

    def bfs(first_night_x, first_night_y, finally_night_x, finally_night_y):
        # 큐 생성
        queue = deque()
        # 큐에 처음 위치 넣어주기
        queue.append((first_night_x, first_night_y)) #튜플로 담김
        
        # 큐에 요소가 없을 때까지 반복
        while queue:
            # 위치를 x, y 변수에 넣어주고 큐에서 삭제
            x, y = queue.popleft()
            # 방문했다고 표시
            visited[x][y] = True

            # 움직이는 방향에 따라 탐색
            for i in range(4):
                # 만약 x로 -2, 2만큼 움직인다면
                if i < 2:
                    # y는 -1, 1으로만 이동할 수 있음
                    for j in range(2):
                        #움직인 x, y값을 변수에 넣어줌
                        move_x = x + dx[i]
                        move_y = y + dy[j]

                        # 만약 움직인 범위가 체스판을 벗어난다면 아무것도 하지않음
                        if move_x < 0 or move_x > L-1 or move_y < 0 or move_y > L-1:
                            continue
                        
                        # 만약 움직인 위치를 방문하지 않았다면
                        if not visited[move_x][move_y]:
                            # 움직인 위치에 이동한 거리인 1만큼을 추가
                            board[move_x][move_y] = board[x][y] + 1
                            # 방문했다고 표시
                            visited[move_x][move_y] = True
                            # 큐에 움직인 위치를 넣어준다
                            queue.append((move_x, move_y))

                        # 만약에 움직인 위치가 최종 도착할 위치와 같다면 지금까지 움직인 거리를 저장한 board[][]를 반환
                        if move_x == finally_night_x and move_y == finally_night_y:
                            return board[move_x][move_y]
                else:
                    # 만약 x가 -1, 1만큼 움직인다면 y는 -2, 2만큼 움직인다.
                    for j in range(2,4):
                        move_x = x + dx[i]
                        move_y = y + dy[j]

                        if move_x < 0 or move_x > L-1 or move_y < 0 or move_y > L-1:
                            continue
                        
                        if not visited[move_x][move_y]:
                            board[move_x][move_y] = board[x][y] + 1
                            visited[move_x][move_y] = True
                            queue.append((move_x, move_y))

                        if move_x == finally_night_x and move_y == finally_night_y:
                            return board[move_x][move_y]

    # 값 출력
    print(bfs(first_night_x, first_night_y, finally_night_x, finally_night_y))
    # 테스트 케이스 한개씩 줄여주기
    Test_case -= 1