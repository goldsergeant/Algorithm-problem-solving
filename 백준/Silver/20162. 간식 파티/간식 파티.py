import sys

n=int(input())
scores=[]
for _ in range(n):
    scores.append(int(sys.stdin.readline()))
dp = [scores[i] for i in range(n)]

for i in range(n):
    for j in range(i):
        if scores[j]<scores[i]:
            dp[i]=max(dp[i],dp[j]+scores[i])

print(max(dp))