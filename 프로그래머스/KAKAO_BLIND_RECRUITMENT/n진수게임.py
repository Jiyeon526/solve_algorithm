alp = {0:'0', 1:'1', 2:'2', 3:'3', 
       4:'4', 5:'5', 6:'6', 7:'7', 
       8:'8', 9:'9', 10: 'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

def solution(n, t, m, p):
    answer = ''
    
    answer = numbers(n)
    answer = my(answer, t, m, p)
    
    return answer

def numbers(n):
    res = ''
    
    for i in range(30000):
        tmp = ''
        
        while i >= n:
            tmp += alp[i % n]
            i = i // n
        
        tmp += alp[i]
        tmp = tmp[::-1]
        res += tmp
    
    return res

def my(answer, t, m, p):
    newAnswer = ''
    i = p - 1
    
    for _ in range(t):
        newAnswer += answer[i]
        i += m
    
    return newAnswer