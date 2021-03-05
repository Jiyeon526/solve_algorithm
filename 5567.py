import sys
from collections import deque

input = sys.stdin.readline

def bfs(friend, N):
    que = deque()
    # 자기자신인 1번노드를 넣어줌
    que.append(1)
    visited = [False]*(N+1)
    visited[1] = True
    # while문안에서 count가 1씩 증가하는데 시작이 자기자신부터여서(자기는 포함하지 않음) -1에서 시작
    count = -1
    # last는 1번 노드와 연결된 노드들을 넣어주는 변수(친구의 친구까지만 세야하므로)
    last = [1]

    while que:
        top = que.popleft()
        # 큐에서 꺼내면 친구수를 하나씩 늘려준다
        count += 1
        
        # 만약 노드가 last에 없다면 친구, 친구의 친구가 아니므로 종료한다.
        if top not in last:
            break
        
        # 노드들을 큐에 넣어주는데 방문했다면 안넣어준다
        for node in friend[top]:
            if visited[node]:
                continue
            visited[node] = True
            que.append(node)
            # 친구의 친구까지만
            if top == 1:
                last.append(node)

    # que에 길이까지 더해주는건 
    # 중간에 while문 종료하는 조건문에서 que안에 노드들이 남아있을 수도 있어서임
    return count + len(que)

# 동기수
N = int(input())
# 연결된 친구
M = int(input())
friend = {}

for i in range(M):
    key, value = map(int, input().split())
    # 연결된 친구를 입력받는데 양쪽에 다 넣어줬다(bfs를 key를 기준으로 탐색하기때문)
    if not key in friend:
        friend[key] = [value]
    if not value in friend:
        friend[value] = [key]
    if (key in friend) and (value in friend):
        if not value in friend[key]:
            friend[key] += [value]
        if not key in friend[value]:
            friend[value] += [key]

print(bfs(friend, N))
