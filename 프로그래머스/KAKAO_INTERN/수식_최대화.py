rank = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [2, 0, 1], [1, 2, 0], [2, 1, 0]]
keyDict = {'+': 0, '-': 1, '*': 2 }

def solution(expression):
    answer = 0
    express = []
    tmp = ''
    for i in range(len(expression)):
        if expression[i].isdigit():
            tmp += expression[i]
        else:
            express.append(tmp)
            express.append(expression[i])
            tmp = ""
    express.append(tmp)
    
    for i in range(6):
        nowMoney = cal(i, express)
        answer = max(nowMoney, answer)
        
    return answer

def cal(now, express):
    num = []
    oper = []
    i = 0
    
    while i < len(express):
        if express[i].isdigit():
            num.append(express[i])
        else:
            i -= 1

        if i + 1 >= len(express): break
    
        if len(oper) != 0 and rank[now][keyDict[oper[-1]]] < rank[now][keyDict[express[i+1]]]:
            num[-1] = op(express[i+1], int(num[-1]), int(express[i+2]))
            i += 1
        else:
            oper.append(express[i+1])
        i = i + 2
    
    i = j = 0
    while len(num) >= 2:
        a = int(num[0])
        b = int(num[1])
        num.pop(0)
        num[0] = op(oper[0], a, b)
        oper.pop(0)
    
    return abs(int(num[0]))

def op(o, a, b):
    tmp = 0
    if o == '+':
        tmp = a + b
    elif o == '-':
        tmp = a - b
    elif o == '*':
        tmp = a * b

    return tmp
            
expression = 	"177-661*999*99-133+221+334+555-166-144-551-166*166-166*166-133*88*55-11*4+55*888*454*12+11-66+444*99"
print(solution(expression))