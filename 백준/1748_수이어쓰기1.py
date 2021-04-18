import sys

input = sys.stdin.readline

N = int(input())
# 입력받은 숫자의 자릿수 계산
N_len = len(str(N))

# count는 자릿수를 저장하기 위한 변수
count = N_len
# 총 자릿수의 합
count_sum = 0
# 해당 자릿수에 몇개의 숫자가 있는지 10, 100, 1000을 기준으로 계산하기 위해
check = 10 ** N_len
while N > 0:
    # num은 해당 구간에있는 총 숫자수 ex) 120 - 100 + 1 = 21
    num = N - check//10 + 1
    # 자릿수와 구간에 있는 숫자를 곱해서 총 자릿수 계산
    # ex) 21*3 = 61(자릿수가 3자리인 숫자들의 총 자릿수 합)
    count_sum += num * count
    # 자릿수가 3인구간을 지나면 그다음 시작은 99부터이므로 check를 이용해서 계산
    N = check//10 - 1
    # 자릿수가 한자리씩 준다
    count -= 1
    # check도 10으로 나눈값으로 다시 넣어줌
    check //= 10
    
print(count_sum)