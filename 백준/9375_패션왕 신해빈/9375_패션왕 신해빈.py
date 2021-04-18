import sys

input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n = int(input())
    clothes = {}

    for _ in range(n):
        name, ctype = map(str, input().split())
        if clothes.get(ctype) == None:
            clothes[ctype] = 1
        else:
            clothes[ctype] += 1

    ans = 1
    for value in clothes.values():
        ans *= (value + 1)
    
    print(ans - 1)

