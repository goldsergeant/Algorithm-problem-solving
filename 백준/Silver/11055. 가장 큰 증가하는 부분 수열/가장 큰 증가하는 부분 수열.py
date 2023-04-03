import sys

n=int(input())
numbers=list(map(int,sys.stdin.readline().split()))
dp=[i for i in numbers]
for i in range(1,n):
    for j in range(i):
        if numbers[i]>numbers[j]:
            dp[i]=max(dp[i],numbers[i]+dp[j])

print(max(dp))