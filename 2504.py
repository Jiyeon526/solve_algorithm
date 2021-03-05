import sys
from collections import deque

input = sys.stdin.readline

def complete(str):
    stack = deque()
    for i in str:
        if len(stack) == 0 and (i == ')' or i == ']'):
            return False
        elif i == '(' or i =='[':
            stack.append(i)
        elif i == ')' and stack[-1] == '(':
            stack.pop()
        elif i == ']' and stack[-1] == '[':
            stack.pop()

    if len(stack) > 0:
        return False
    return True

def total(str):
    sum_total = 0
    stack = deque()

    for i in str:
        if i == '(' or i =='[':
            stack.append(i)
        elif i == ')' and stack[-1] == '(':
            stack.pop()
            stack.append(2)
        elif i == ')' and stack[-1] > 0:
            _sum = 0
            for j in range(len(stack)-1,-1,-1):
                if stack[j] == '(':
                    stack.pop()
                    break
                _sum += stack[j]
                stack.pop()
            stack.append(2 * _sum)

        elif i == ']' and stack[-1] == '[':
            stack.pop()
            stack.append(3)
        elif i == ']' and stack[-1] > 0:
            _sum = 0
            for j in range(len(stack)-1,-1,-1):
                # print("J = ", j)
                # print("iter ", stack)
                if stack[j] == '[':
                    # print("out")
                    stack.pop()
                    break
                _sum += stack[j]
                stack.pop()
            stack.append(3 * _sum)
        # print(stack)
    return stack
        
str = input()
if complete(str):
    answer = 0
    result = total(str)
    for i in result:
        answer += i
    print(answer)
else:
    print(0)

    