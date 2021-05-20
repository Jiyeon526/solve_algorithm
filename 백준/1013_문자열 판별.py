import sys

input = sys.stdin.readline

def check():
    i = 0
    while i < len(log):
        print("idx = ", i, " log[i] =", log[i])
        if log[i] == '0':
            if i+1 < len(log) and log[i+1] == '1':
                i = i+2
                continue
            else:
                print('NO')
                return
        else:
            zero = 0
            j = i+1
            while j < len(log):
                if log[j] == '0':
                    zero += 1
                    j += 1
                else:
                    if zero < 2:
                        print('NO')
                        return
                    else:
                        # i = j
                        break
            i = j
            print("middle = ", i, " ", len(log))
            if i < len(log) and log[i] == '1':
                j = i+1
                if i == len(log) - 1:
                    print('YES')
                    return

                one = 0
                origin_i = i  
                while j < len(log):
                    if log[j] == '1':
                        j += 1
                        one += 1
                    else:
                        if j+1 < len(log) and log[j+1] == '1':
                            i = j+2
                        else:
                            if one > 1:
                                i = j - 1
                            else:
                                print('NO')
                                return
                        break
                if origin_i == i:
                    print('YES')
                    return
            else:
                print('NO')
                return
    print('YES')
    return

TC = int(input())
while(TC > 0):
    TC -= 1
    log = input().strip()
    check()




                
            