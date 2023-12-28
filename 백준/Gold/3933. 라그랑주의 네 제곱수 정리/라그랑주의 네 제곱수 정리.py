import sys
MAX_NUM=2**15
dp=[[0 for _ in range(4+1)] for _ in range(MAX_NUM+1)]
for i in range(1,int(MAX_NUM**(1/2))+1):
    dp[i*i][1]=1

    for j in range(i*i,MAX_NUM+1):
        dp[j][2]+=dp[j-i*i][1]
        dp[j][3]+=dp[j-i*i][2]
        dp[j][4]+=dp[j-i*i][3]


while True:
    N=int(sys.stdin.readline())
    if N==0:
        break

    print(sum(dp[N]))