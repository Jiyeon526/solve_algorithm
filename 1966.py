import sys
from collections import deque

input = sys.stdin.readline

# 큐중에서 max값을 찾는함수
def find_max(que, N):
    # 큐의 첫번째값을 넣어줌
    max_import = que[0][0]

    # 하나씩 비교하면서 큐중에서 max값을 찾음
    for idx in range(1, N):
        if max_import < que[idx][0]:
            max_import = que[idx][0]
    
    # max값 반환
    return max_import

# 언제 출력되는지 반환하는 함수
def print_paper(important, N, find_num):
    que = deque()
    count = 0

    # 큐에 중요도와 순서를 넣어준다.
    for idx in range(N):
        que.append((important[idx], idx))

    # 중요도중에서 max값을 찾는다
    max_import = find_max(que, len(que))

    while que:
        # 큐에서 첫번째를 뽑아서 넣어줌
        impo, idx = que.popleft()

        # 만약 중요도가 max값보다 낮다면 다시 큐에 넣어준다
        if impo < max_import:
            que.append((impo, idx))
        else:
            # 만약 max값이라면 카운트를 하나 올리고(출력 순서)
            count += 1
            # 그 인덱스번호가 찾는 순서였다면 count값을 반환한다.
            if idx == find_num:
                return count
            # max값을 다시 찾아준다.
            max_import = find_max(que, len(que))

Test_case = int(input())

while Test_case > 0:
    N, find_num = map(int, input().split())
    important = list(map(int, input().split()))
    print(print_paper(important, N, find_num))

    Test_case -= 1