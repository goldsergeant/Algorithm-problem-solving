import sys

N=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
dp=[0 for _ in range(max(numbers)+1)]

answer=0
for i in range(N):
    dp[numbers[i]]=1
    dp[numbers[i]]+=dp[numbers[i]-1]
    answer=max(answer,dp[numbers[i]])

print(N-answer)