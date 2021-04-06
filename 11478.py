import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

s = input().strip()
lenght = len(s)
lst = set()

def comb(m, cnt):
    if m not in lst:
        lst.add(m)
    if cnt >= lenght:
        return
    
    m += s[cnt+1:cnt+2]
    comb(m, cnt+1)

for i in range(lenght):
    start = s[i]
    lst.add(start)
    comb(start, i)

print(len(lst))
