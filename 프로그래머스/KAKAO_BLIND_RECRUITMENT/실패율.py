def solution(N, stages):
    answer = []
    playerCnt = [0] * (N + 2)
    notClearCnt = [0] * (N + 2)
    
    for s in stages:
        notClearCnt[s] += 1

    for i in range(len(notClearCnt)-2, 0, -1):
        if i == N:
            playerCnt[i] = notClearCnt[i+1] + notClearCnt[i]
        else: playerCnt[i] = notClearCnt[i] + playerCnt[i+1]
    
    rate = {}
    for i in range(1, N+1):
        r = notClearCnt[i]/playerCnt[i] if playerCnt[i] != 0 else 0
        if r not in rate:
            rate[r] = []
        rate[r].append(i)

    rate_sort = sorted(rate.items(), reverse = True)
    for r, stages in rate_sort:
        for s in stages:
            answer.append(s)
            
    return answer