import sys
from collections import defaultdict,Counter

N=int(sys.stdin.readline())
boss=list(map(int,sys.stdin.readline().split()))
tree=defaultdict(list)
dp=[0 for _ in range(N+1)]
for num,b in enumerate(boss):
    if b!=-1:
        tree[b].append(num)

def post_order(n):
    if dp[n]!=0:
        return dp[n]

    arr=sorted([post_order(next_node) for next_node in tree[n]],reverse=True)
    if arr:
        for i in range(len(arr)):
            dp[n]=max(dp[n],arr[i]+i+1)

    return dp[n]

print(post_order(0))
