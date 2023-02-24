import sys

n,m=map(int,sys.stdin.readline().split())
trees=list(map(int,sys.stdin.readline().split()))
left=1
right=max(trees)
while left<=right:
    cut_height= (right + left) // 2
    cut_tree=0
    for tree in trees:
        cut_tree+=max(tree - cut_height, 0)

    if cut_tree>=m:
        left=cut_height+1
    else:
        right=cut_height-1

print(right)