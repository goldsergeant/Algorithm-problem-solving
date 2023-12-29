import copy
import sys

N,M=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp=copy.deepcopy(board)
for i in range(N):
    for j in range(M):
        for ny,nx in [(i+1,j),(i,j+1),(i+1,j+1)]:
            if 0<=ny<N and 0<=nx<M:
                dp[ny][nx]=max(dp[ny][nx],dp[i][j]+board[ny][nx])

print(dp[-1][-1])