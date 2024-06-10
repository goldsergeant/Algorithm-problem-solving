import sys
sys.setrecursionlimit(10000)

N=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
dp1=[[-1 for _ in range(N)] for _ in range(N)]
dp2=[-1 for _ in range(N)]
def is_panlindrome(left,right):
    if left>=right:
        return 1
    if dp1[left][right]!=-1:
        return dp1[left][right]

    if numbers[left]!=numbers[right]:
        dp1[left][right]=0
    else:
        dp1[left][right]=is_panlindrome(left+1,right-1)
    return dp1[left][right]

def dfs(idx):
    if idx>=N:
        return 0
    if dp2[idx]!=-1:
        return dp2[idx]

    dp2[idx]=0
    if is_panlindrome(idx,N-1):
        dp2[idx]=1

    for next_idx in range(idx+1,N-2,2):
        if is_panlindrome(idx,next_idx) and dfs(next_idx+1)>0:
            dp2[idx]=max(dp2[idx],dfs(next_idx+1)+1)
    return dp2[idx]

print(dfs(0) or -1)
