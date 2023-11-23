import itertools

import math
import sys

n,c=map(int,sys.stdin.readline().split())
weights=list(map(int,sys.stdin.readline().split()))
answer=0
def dfs(start,end,part:list,total):
    if start>end:
        part.append(total)
        return
    dfs(start+1,end,part,total+weights[start])
    dfs(start+1,end,part,total)

part1=[]
part2=[]
dfs(0,n//2-1,part1,0)
dfs(n//2,n-1,part2,0)
part2.sort()
for part1_sum in part1:
    if part1_sum>c:
        continue
    left=0
    right=len(part2)
    target=c-part1_sum
    while left<right:
        mid=(left+right)//2
        if part2[mid]>target:
            right=mid
        elif part2[mid]<=target:
            left=mid+1
    answer+=right

print(answer)
