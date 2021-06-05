import sys

def find(a):
    if uf[a]==a: return a
    uf[a] = find(uf[a])
    return uf[a]

def union(a, b):
    aa = find(a)
    bb = find(b)
    
    if aa != bb:
        uf[bb] = aa
        number[aa] += number[bb]

T = int(input())

for _ in range(T):
    F = int(input())
    uf = dict()
    number = dict()

    for _ in range(F):
        a, b = map(str, input().split())

        if a not in uf:
            uf[a] = a
            number[a] = 1
        if b not in uf:
            uf[b] = b
            number[b] = 1
        
        union(a, b)
        print(number[find(a)])