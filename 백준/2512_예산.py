import sys

city = int(input())
money = list(map(int, input().split()))
total = int(input())

if sum(money) <= total:
    print(max(money))
else:
    start = 0
    end = total
    ans = 0
    while start<=end:
        mid = (start+end)//2

        midSum = 0
        for m in money:
            if m <= mid:
                midSum += m
            else:
                midSum += mid
        
        if midSum <= total:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
        
    print(ans)