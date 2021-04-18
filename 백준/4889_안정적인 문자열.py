import sys

input = sys.stdin.readline
t = 1
while True:
    S = input().strip()
    if '-' in S:
        break

    stack = []
    cnt = 0
    for i in range(len(S)):
        if S[i] == '}':
            if len(stack) == 0:
                stack.append('{')
                cnt += 1
            elif stack[-1] == '{':
                stack.pop()
            else:
                stack.append('{')
                cnt += 1
        else:
            stack.append('{')
    
    if len(stack) != 0:
        cnt += len(stack)//2

    ans = str(t) + ". " + str(cnt)
    print(ans)
    t += 1