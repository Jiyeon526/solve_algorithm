import sys
sys.setrecursionlimit(10**9)

def search(arr):
    # print(arr)
    if len(arr) == 1:
        print(arr[0])
        return
    
    idx = len(arr)
    root = arr[0]
    for i in range(len(arr)):
        if root < arr[i]:
            idx = i
            break
    
    if idx > 1:
        search(arr[1:idx])
    
    if idx < len(arr):
        search(arr[idx:])
    print(root)

tree = []
while True:
    try:
        n = int(input())
        tree.append(n)
    except:
        break

search(tree)


