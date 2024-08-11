import sys

def find_bisect(left,right):
    end=right
    while left+1<right:
        mid=(left+right)//2
        target=pictures[mid]

        if pictures[end][0]-target[0]>=S:
            left=mid
        else:
            right=mid

    return left

N,S=map(int,sys.stdin.readline().split())
pictures=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
pictures.sort()
dp=[0 for _ in range(N)]
dp[0]=pictures[0][1]

for i in range(1,N):
    idx=find_bisect(0,i)
    if pictures[i][0]-pictures[idx][0]>=S:
        dp[i]=max(dp[idx]+pictures[i][1],dp[i-1])
    else:
        dp[i]=max(pictures[i][1],dp[i-1])

print(dp[-1])
