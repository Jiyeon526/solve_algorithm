def solution(p):
    if isOk(p):
        return p
    return isPerfect(p)

def isOk(P):
    lst = []
    for p in P:
        if p == '(':
            lst.append(p)
        elif len(lst) != 0 and p == ')' and lst[-1] == '(':
            lst.pop()
        else:
            return False
    return True

def isPerfect(P):
    if P == "": return P
    
    cnt_R = 0; cnt_L = 0; idx = 0
    for i in range(len(P)):
        if P[i] == '(':
            cnt_R += 1
        else:
            cnt_L += 1
        if cnt_R == cnt_L:
            idx = i+1
            break
    
    u = P[:idx]
    if idx >= len(P):
        v = ""
    else: v = P[idx:]
    if isOk(u):
        return u + isPerfect(v)
    else:
        V = isPerfect(v)
        U = ""
        for i in range(1, len(u) - 1):
            if u[i] == '(': U += ')'
            else: U += '('
        return '(' + V + ')' + U