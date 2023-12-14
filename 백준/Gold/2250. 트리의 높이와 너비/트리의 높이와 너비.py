import collections
import sys

N = int(sys.stdin.readline())
LEFT=0
RIGHT=1
tree=[[-1,-1] for _ in range(N+1)]
visited_cols=[False]*(N+1)
level_col=[[] for _ in range(N + 1)]
can_root_node=[True]*(N+1)
root_node=0

def inorder(node, level):
    left=tree[node][LEFT]
    right=tree[node][RIGHT]

    if left!=-1:
        col=inorder(left, level + 1)

    col=1
    while visited_cols[col]:
        col+=1
    visited_cols[col]=True
    level_col[level].append(col)

    if right!=-1:
        inorder(right,level+1)


for _ in range(N):
    root, left, right = map(int, sys.stdin.readline().split())
    if left != -1:
        tree[root][LEFT] = left
        can_root_node[left]=False
    if right != -1:
        tree[root][RIGHT]=right
        can_root_node[right]=False

root_node=can_root_node[1:].index(True)+1

inorder(root_node,1)
answer=(0,0)
for i in range(1,N+1):
    arr=level_col[i]
    if not arr:
        break
    width=max(arr)-min(arr)+1
    if answer[1]<width:
        answer=(i,width)

print(*answer)