import sys
from typing import List

T=int(sys.stdin.readline())

def build_tree(preorder:List[int],inorder:List[int]):
    if inorder:
        idx=inorder.index(preorder.pop(0))

        node=inorder[idx]
        tree[node][0]=build_tree(preorder,inorder[:idx])
        tree[node][1]=build_tree(preorder,inorder[idx+1:])

        return node
    return 0

def post_order(root):
    if tree[root][0]!=0:
        post_order(tree[root][0])
    if tree[root][1]!=0:
        post_order(tree[root][1])

    print(root,end=' ')
for _ in range(T):
    N=int(sys.stdin.readline())
    tree=[[0,0] for _ in range(N+1)]
    preorder=list(map(int,sys.stdin.readline().split()))
    inorder=list(map(int,sys.stdin.readline().split()))
    root=preorder[0]
    build_tree(preorder,inorder)
    post_order(root)

    print()