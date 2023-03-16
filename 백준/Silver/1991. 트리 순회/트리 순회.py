import sys

n=int(input())
tree=dict()
for _ in range(n):
    root,left,right=sys.stdin.readline().split()
    tree[root]=(left,right)

def preorder(root):
    if root != '.':
        left = tree[root][0]
        right = tree[root][1]
        print(root, end='')
        preorder(left)
        preorder(right)

def inorder(root):
    if root != '.':
        left = tree[root][0]
        right = tree[root][1]
        inorder(left)
        print(root, end='')
        inorder(right)

def postorder(root):
    if root != '.':
        left = tree[root][0]
        right = tree[root][1]
        postorder(left)
        postorder(right)
        print(root,end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')

