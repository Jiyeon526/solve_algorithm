import sys

def preorder(root):
    print(chr(root + 64), end="")
    
    if node[root][0] != 0:
        preorder(node[root][0])
    if node[root][1] != 0:
        preorder(node[root][1])
    return

def inorder(root):
    if node[root][0] != 0:
        inorder(node[root][0])
    
    print(chr(root + 64), end="")

    if node[root][1] != 0:
        inorder(node[root][1])
    return
    
def postorder(root):
    if node[root][0] != 0:
        postorder(node[root][0])
    
    if node[root][1] != 0:
        postorder(node[root][1])

    print(chr(root + 64), end="")

    return

N = int(input())
node = [[0, 0] for _ in range(N+1)]

for i in range(1, N+1):
    root, left, right = map(str, input().split())
    if left != '.':
        node[ord(root)-64][0] = ord(left) - 64
    if right != '.':
        node[ord(root)-64][1] = ord(right) - 64

preorder(1)
print()
inorder(1)
print()
postorder(1)