import sys

N,M=map(int,sys.stdin.readline().split())
board=[sys.stdin.readline().rstrip()for _ in range(N)]
dp=[[0]*M for _ in range(N)]
pos=[(0,-1),(-1,0),(-1,-1)]
answer=0
for i in range(N):
    for j in range(M):
        if board[i][j]=='1':
            dp[i][j]=1
            answer=1

for i in range(1,N):
    for j in range(1,M):
        if board[i][j]=='1':
            if all(board[dy+i][dx+j]!='0' for dy,dx in pos):
                dp[i][j]=min([dp[i+dy][j+dx] for dy,dx in pos])+1
                answer=max(answer,dp[i][j]**2)

print(int(answer))