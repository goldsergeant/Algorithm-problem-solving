import sys

MOD_NUM=1000000009
N,M=map(int,sys.stdin.readline().split())
board=[list(sys.stdin.readline().rstrip()) for _ in range(N)]
dp=[[1 for _ in range(M)] for _ in range(N)]
answer_x,answer_y=0,0

for i in range(N):
    for j in range(M):
        # if dp[i][j]==0:
        #     dp[i][j]=1

        if board[i][j]=='E':
            dp[i][j+1]=(dp[i][j+1]+dp[i][j])%MOD_NUM
        elif board[i][j]=='S':
            dp[i+1][j]=(dp[i+1][j]+dp[i][j])%MOD_NUM
        elif board[i][j]=='B':
            dp[i][j+1]=(dp[i][j+1]+dp[i][j])%MOD_NUM
            dp[i+1][j]=(dp[i+1][j]+dp[i][j])%MOD_NUM
        else:
            answer_x,answer_y=i,j

print(dp[answer_x][answer_y])