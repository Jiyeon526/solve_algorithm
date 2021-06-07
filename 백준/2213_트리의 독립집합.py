import sys
sys.setrecursionlimit(10**9)

def dfs(r):
    cnt[r][0] = w[r] # 나 포함
    visit[r] = True
    num[r][0].append(r)

    for i in tree[r]:
        if not visit[i]:
            dfs(i)
            cnt[r][0] += cnt[i][1] # 다른건 안포함
            num[r][0] += num[i][1]

            if cnt[i][0] > cnt[i][1]:
                cnt[r][1] += cnt[i][0]
                num[r][1] += num[i][0]
            else:
                cnt[r][1] += cnt[i][1]
                num[r][1] += num[i][1]

n = int(input())
w = [0] + list(map(int, input().split()))
tree = [[] for _ in range(n+1)]
cnt = [[0, 0] for _ in range(n+1)]
visit = [False] * (n+1)
num = [[[], []] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dfs(1)

if cnt[1][0] > cnt[1][1]:
    print(cnt[1][0])
    ans = num[1][0]
else:
    print(cnt[1][1])
    ans = num[1][1]

ans.sort()
print(*ans)