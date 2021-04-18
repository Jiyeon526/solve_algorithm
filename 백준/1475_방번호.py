import sys

input = sys.stdin.readline

# 방번호
room = int(input())
# 빙반호 복사
clone = room
# 몇 세트가 쓰였는지 확인용도
set_number = [0 for _ in range(10)]
# 6과 9 체크
check = 0
# 답
answer = 0

while room > 0:
    # 방번호중 끝번호를 인덱스로 사용 EX) 9999 -> 9
    idx = room % 10
    # 방번호는 한자리 줄여준다
    room //= 10
    # 인덱스에 하나 추가
    set_number[idx] += 1

    # 만약 인덱스가 6이나 9인데 체크하는게 1이면(6또는 9가 2번나왔으면)
    if (idx == 6 or idx == 9) and check == 1:
        # 그 인덱스 번호 하나 줄여주고 체크는 다시 0으로
        set_number[idx] -= 1
        check = 0
    # 만약 인덱스가 6이나 9인데 체크가 안되있으면
    elif (idx == 6 or idx == 9) and check == 0:
        # 체크를 1로 바꿔줌
        check = 1

# 만약 원래 숫자가 10이라면  while문을 수행안하니깐 그냥 1세트썻다고 적어줌 
if clone < 10:
    answer = 1
else:
    # 6과 9를 더해주고 하나는 초기화
    set_number[6] += set_number[9]
    set_number[9] = 0
    # 최대값이 총 사용한 세트개수
    answer = max(set_number)

print(answer)
