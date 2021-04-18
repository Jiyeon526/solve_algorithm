import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()
P = "I" + "OI" * N # 찾을 문자열 만들기

plen = len(P)
idx = 0
ans = 0
check = False # 이어지는 문자열인지 확인

while idx <= M:
    if check:
        if S[idx:idx+2] == "OI": 
            ans += 1
            idx = idx+2
        else:
            check = False # 만약 아니라면 check를 풀어서 다시 I부터 비교하게 하기
    else:
        if S[idx] == "I": # 문자열 맨 앞비교
            if S[idx:idx+plen] == P: # 문자열을 p의 길이만큼 잘라서 p와 같은지 확인하기
                check = True
                ans += 1
                idx = idx + plen
            else:
                idx += 1
        else:
            idx += 1

print(ans)