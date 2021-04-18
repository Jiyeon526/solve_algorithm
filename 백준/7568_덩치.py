import sys

input = sys.stdin.readline

# 사람 수 입력
Person_number = int(input())
Person = []

# 사람들의 몸무게와 키를 입력받음
for i in range(Person_number):
    Person.append(list(map(int, input().split())))

# 사람들의 몸무게와 키를 비교
for i in range(Person_number):
    # 덩치 등수
    rank = 1
    for j in range(Person_number):
        # 만약 같은 사람이라면 그냥 넘김
        if i == j:
            continue
        # 만약 나보다 덩치가 큰(몸무게와 키가 더 큰)사람이 있다면 덩치 등수를 1씩 올림
        if Person[i][1] < Person[j][1] and Person[i][0] < Person[j][0]:
            rank += 1
    print(rank, end=' ')
