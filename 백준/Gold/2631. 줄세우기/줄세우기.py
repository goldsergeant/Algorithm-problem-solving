import sys

n=int(input())
answer=0
children=[]
dp=[1 for i in range(n)]
for _ in range(n):
    children.append(int(sys.stdin.readline().rstrip()))

for i in range(1,n):
    for j in range(0,i):
        if children[j]<children[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))
