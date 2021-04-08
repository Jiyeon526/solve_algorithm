import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    S = input().strip()
    slen = len(S)
    i = 0; j = slen-1
    pseudo = False
    ans = 2
    # print(slen, slen//2)
    while(i <= slen//2 and slen//2 <= j < slen):
        # print(i, j, S[i], S[j])
        if j == i:
            if pseudo:
                ans = 1
            else: ans = 0
            break
        if j-i == 1 :
            if S[i] == S[j]:
                if pseudo:
                    ans = 1
                else: ans = 0
            else:
                if pseudo:
                    break
                else:
                    ans = 1

        tmpi = i
        tmpj = j
        if S[i] == S[j]:
            i += 1
            j -= 1
        elif S[i+1] == S[j] and not pseudo:
            pseudo = True
            i += 2
            j -= 1

        if tmpi == i and tmpj == j:
            break

    if pseudo and S[i] == S[j]:
        ans = 1
    
    if ans == 2:
        slen = len(S)
        i = 0; j = slen-1
        pseudo = False
        while(i <= slen//2 and slen//2 <= j < slen):
            # print(i, j, S[i], S[j])
            if j == i:
                if pseudo:
                    ans = 1
                else: ans = 0
                break
            if j-i == 1 :
                if S[i] == S[j]:
                    if pseudo:
                        ans = 1
                    else: ans = 0
                else:
                    if pseudo:
                        break
                    else:
                        ans = 1

            tmpi = i
            tmpj = j
            if S[i] == S[j]:
                i += 1
                j -= 1
            elif S[i] == S[j-1] and not pseudo:
                pseudo = True
                i += 1
                j -= 2
            
            if tmpi == i and tmpj == j:
                break


        if pseudo and S[i] == S[j]:
            ans = 1
    print(ans)