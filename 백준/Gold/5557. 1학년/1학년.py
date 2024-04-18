import sys
sys.setrecursionlimit(100000)

N=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
dp=[[0 for _ in range(20+1)] for _ in range(N)]

dp[0][numbers[0]]=1
for i in range(N-1):
    if i<N-2:
        for j in range(0,20+1):
            n_num=j+numbers[i+1]
            if 0<=n_num<=20:
                dp[i+1][n_num]+=dp[i][j]
            n_num= j-numbers[i+1]
            if 0<=n_num<=20:
                dp[i+1][n_num]+=dp[i][j]
    else:
        for j in range(0,20+1):
            if j==numbers[i+1]:
                dp[i+1][j]+=dp[i][j]

print(dp[-1][numbers[-1]])