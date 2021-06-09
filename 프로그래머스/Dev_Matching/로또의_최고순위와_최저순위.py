def solution(lottos, win_nums):
    answer = []
    nums = [False] * 46
    zero_cnt = 0
    win_cnt = 0
    
    for i in win_nums:
        nums[i] = True
    
    for i in lottos:
        if i == 0: zero_cnt += 1
        if nums[i]: win_cnt += 1
            
    high = 7 - (zero_cnt + win_cnt)
    low = 7 - win_cnt
    
    if high >= 6: high = 6
    if low >= 6: low = 6
    
    answer.append(high)
    answer.append(low)
        
    return answer