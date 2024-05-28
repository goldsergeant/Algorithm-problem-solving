import collections
import sys


N=int(sys.stdin.readline())
opened_doors=list(map(int,sys.stdin.readline().split()))
L=int(sys.stdin.readline())
use_doors=list(int(sys.stdin.readline()) for _ in range(L))
dp=[[[-1 for _ in range(L)] for _ in range(N+1)] for _ in range(N+1)]

def dfs(one,two,depth):
    if depth==L:
        return 0
    if dp[one][two][depth]!=-1:
        return dp[one][two][depth]
    dp[one][two][depth]=0
    use_door=use_doors[depth]
    dp[one][two][depth]=min(dfs(use_door,two,depth+1)+abs(one-use_door),dfs(one,use_door,depth+1)+abs(two-use_door))
    return dp[one][two][depth]

print(dfs(opened_doors[0],opened_doors[1],0))