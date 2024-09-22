import sys
from math import comb

def dfs(idx,cnt):
    global target
    if dp[idx][cnt]!=-1:
        return dp[idx][cnt]

    if cnt==3:
        if t_sum[-1]-t_sum[idx]==target:
            dp[idx][cnt]=1
            return dp[idx][cnt]
        dp[idx][cnt]=0
        return 0

    tmp=0
    for i in range(idx,N):
        val = t_sum[i]-t_sum[idx]
        if val==target:
            tmp+=dfs(i,cnt+1)

    dp[idx][cnt]=tmp
    return dp[idx][cnt]

N=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
t_sum=[0 for _ in range(N)]
t_sum[0]=numbers[0]
for i in range(1,N):
    t_sum[i]= t_sum[i - 1] + numbers[i]

if t_sum[-1]==0:
    print(comb(t_sum.count(0)-1, 3))
elif t_sum[i]%4!=0:
    print(0)
else:
    target= t_sum[-1] // 4
    dp=[[-1 for _ in range(4+1)] for _ in range(N+1)]
    answer=0
    for i in range(N):
        if t_sum[i]==target:
            answer+=dfs(i,1)
    print(answer)
