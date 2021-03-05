import sys

input = sys.stdin.readline

K = int(input())
money_list = []

for i in range(K):
    # 값을 하나씩 입력을 받는다.
    money = int(input())
    # 만약 입력받은 값이 0이고 리스트에 숫자가 담겨있으면 마지막에 append된 숫자를 빼준다.
    if money == 0 and len(money_list) > 0:
        money_list.pop()
    else:
        # 그렇지 않다면 값을 넣어준다.(0은 더해도 0이므로 첫번째에 넣어줘도 상관없음)
        money_list.append(money)

print(sum(money_list))

#파이썬에서 스택 라이브러리가 없고 그냥 리스트로 대체한다