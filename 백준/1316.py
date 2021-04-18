import sys

# 그룹 단어인지 체크하는 함수
def check(words): 
    # words에 첫번째 단어를 넣어줌
    group = [words[0]]

    for idx in range(1, len(words)):
        # 만약 내 뒤에있는 알파벳이랑 다른데 group에 내 알파벳이 있다면 그룹단어가 아님
        # words = ababc, group = a, b인데 3번째인 a가 다시 들어오려하는 상황
        if words[idx] != words[idx-1] and words[idx] in group:
            return 0
        # 내 뒤에있는 알파벳이랑 다른데 group에 없을 경우 추가
        elif words[idx] != words[idx-1] and words[idx] not in group:
            group.append(words[idx])
    return 1     
        
        
input = sys.stdin.readline

Test_case = int(input())
count = 0

while Test_case > 0:
    words = input()
    # words가 그룹단어면 1, 아니면 0 더해준다
    count += check(words)
    Test_case -= 1

print(count)