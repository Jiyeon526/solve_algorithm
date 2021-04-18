import sys

input = sys.stdin.readline

num1 = input().strip()
num2 = input().strip()
lst = {
    'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
    'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000
}
reverse_lst = dict(map(reversed, lst.items()))

for i in range(4):
    for j in range(1, 10):
        tmp = (10**i) * j
        pre_tmp = (10**i) * (j-1)
        if tmp in reverse_lst:
            continue
        else:
            s = reverse_lst[pre_tmp]
            t = tmp - pre_tmp
            s += reverse_lst[t]
            reverse_lst[tmp] = s

def toNum(num):
    idx = 0
    ans = 0

    while idx < len(num) - 1:
        if lst[num[idx]] >= lst[num[idx+1]]:
            ans += lst[num[idx]]
            idx += 1
        else:
            ans += lst[num[idx:idx+2]]
            idx += 2
    
    if idx < len(num):
        ans += lst[num[idx]]

    return ans

N1 = toNum(num1)
N2 = toNum(num2)
N = N1 + N2
print(N)
sN = str(N)
r = 10**(len(sN)-1)
ans = ''

for i in range(len(sN)):
    c = int(sN[i]) * r
    r //= 10
    if c == 0:
        continue
    ans += reverse_lst[c]
    
    
print(ans)