alpha = [0 for _ in range(26)]
result = []
max_cnt = 0
max_arr = []
check = [False for _ in range(26)]

def solution(orders, course):
    global check
    global result
    global max_cnt
    global max_arr
    global alpha

    answer = []

    for s in orders:
        for i in range(len(s)):
            alpha[ord(s[i]) - 65] += 1

    for c in course:
        comb(0, 0, c, orders)
        for a in max_arr:
            answer.append(a)
        result = []
        max_cnt = 0
        max_arr = []
        check = [False for _ in range(26)]
       
    answer.sort()
    return answer

def comb(idx, cnt, total, orders):
    global check
    global result
    global max_cnt
    global max_arr
    global alpha

    if cnt == total:
        tmp = isCnt(orders, result)
        join_str = "".join(result)
        # print("tmp: ", tmp, "joion_str = ", join_str)
        if tmp >= 2 and max_cnt < tmp:
            max_arr.clear()
            max_cnt = tmp
            max_arr.append(join_str)
        elif tmp >= 2 and max_cnt == tmp:
            max_arr.append(join_str)
        # print("max_cnt = ", max_cnt, "max_arr = ", max_arr)
        return
    
    if idx > 26: return
    
    for i in range(idx, 26):
        if alpha[i] != 0 and not check[i]:
            result.append(chr(i+65))
            check[i] = True
            comb(i+1, cnt+1, total, orders)
            check[i] = False
            result = result[:-1]  


def isCnt(orders, result):
    count = 0
    
    for s in orders:
        no = False
        for c in result:
            if c not in s: 
                no = True
                break
        if not no:
            count += 1

    return count