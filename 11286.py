import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

while N > 0:
    N -= 1
    num = int(input())
    if num == 0:        
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(num), num))



