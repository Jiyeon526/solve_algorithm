import sys

input = sys.stdin.readline

# 숫자입력받기
N =  int(input())
num = []

for i in range(N):
    num.append(int(input()))

# 전체 갯수
length = len(num)
# 평균계산(첫째자리 반올림)
avg = round(sum(num) / length)
# 중간값을 구하기 위해 정렬한다.
num.sort() #nlogn
# 중간값 구하기
middle = num[length//2]
# num리스트의 범위
ran = num[length-1] - num[0]

# 최빈값 구하기
# 각 숫자가 몇개있는지 담는 딕셔너리만들기
num_count = {}
for i in range(N):
    # 키값으로 숫자주기 ex) num = [1,1,3,8] => 키값은 1,3,8
    key = num[i]
    # 만약 키가 있지않다면 1로 초기값 설정
    if num_count.get(key) == None:
        num_count[key] = 1
    # 키가 있다면 1씩 더해준다 ex) num_count[1] = 2가 됨
    else:
        num_count[key] += 1

#카운트 시간복잡도 n인데 for문안에있어서 n^2그래서 최대 50만제곱을 돌면 시간초과가 난다
# 카운트한 숫자들 중 최대값을 찾아서 max_list에 넣어준다.
max_list = []
max_value = max(num_count.values())
for key, value in num_count.items():
    # 만약 최대 카운트수와 현재 value값이 같다면
    if max_value == num_count[key]:
        # 리스트에 키값을 넣어준다
        max_list.append(key)

# 만약 리스트의 길이가 1이라면 최빈값이 1개이므로 리스트의 첫번째값이 답
if len(max_list) == 1:
    max_count = max_list[0]
else:
    # 그렇지 않다면 최빈값이 여러개이므로 최빈값중 두번째 숫자가 답
    max_count = max_list[1]

print(avg)
print(middle)
print(max_count)
print(ran)  




































#시간 초과
# import sys

# input = sys.stdin.readline

# N =  int(input())
# num = []

# for i in range(N):
#     num.append(int(input()))

# avg = round(sum(num) / len(num))
# num.sort()
# middle = num[len(num)//2]
# ran = num[len(num)-1] - num[0]

# num_count = {}
# max_value = 0
# for i in range(N):
#     key = num[i]
#     value = num.count(num[i])
#     num_count[key] = value

#     if max_value < value:
#         max_value = value

# max_list = []
# for key, value in num_count.items():
#     if max_value == num_count[key]:
#         max_list.append(key)

# if len(max_list) == 1:
#     max_count = max_list[0]
# else:
#     max_count = max_list[1]

# print(avg)
# print(middle)
# print(max_count)
# print(ran)  

























# num_count = []
# for i in range(N):
#     con = num.count(num[i])
#     num_count.append(con)

# max_count = max(num_count)
# second = 0
# print("num ", num_count)
# print("max ", max_count)
# for i in range(N):
#     print("count ", num_count.count(max_count))
#     if num_count.count(max_count) > 2:
#         if num_count[i] == max_count and (second == 1 or len(num) == 1):
#             answer_count = num[i]
#             break;
#         elif num_count[i] == max_count:
#             second = 1
#     elif num_count[i] == max_count:
#         answer_count = num[i]


# print(answer_count)
   