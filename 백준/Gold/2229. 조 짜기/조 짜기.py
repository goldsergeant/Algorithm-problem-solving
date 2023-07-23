import sys

n=int(input())
students=list(map(int,sys.stdin.readline().split()))
students.insert(0,0)
dp=[0 for _ in range(10001)]
max_diff=0
for i in range(1,n+1):
    for j in range(i,0,-1):
        dp[i]=max(dp[i],max(students[j:i+1])-min(students[j:i+1])+dp[j-1])
print(dp[n])