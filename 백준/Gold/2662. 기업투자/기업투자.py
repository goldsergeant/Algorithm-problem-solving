import sys

N,M=map(int,sys.stdin.readline().split())
profits=[[0]*(M+1)] # [금액][회사]
dp=[[0 for _ in range(N+1)] for _ in range(M+1)] # [회사][금액]
path=[[(0,0) for _ in range(N + 1)] for _ in range(M + 1)] # [회사][금액]
for _ in range(N):
    arr=list(map(int,sys.stdin.readline().split()))
    profits.append([0]+arr[1:])

for i in range(1,M+1):
    for j in range(N+1):
        for k in range(j+1):
            prev_money=j-k
            cost=dp[i-1][prev_money]+profits[k][i]
            if dp[i][j]<cost:
                dp[i][j]=cost
                path[i][j]=(i-1,prev_money)

money=N
i=M
answer=[]
while i>0 and money>=0:
    prev_i,prev_money=path[i][money]
    answer.append(money-prev_money)
    i,money=prev_i,prev_money

print(dp[M][N])
print(*answer[::-1])