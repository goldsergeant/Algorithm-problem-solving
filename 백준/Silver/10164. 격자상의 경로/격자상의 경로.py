import sys

def dfs(r,c,er,ec):
    if r==er and c==ec:
        return 1
    if dp[r][c]!=-1:
        return dp[r][c]

    dp[r][c]=0
    for dy,dx in (1,0),(0,1),:
        nr,nc=dy+r,dx+c
        if nr>er or nc>ec:
            continue
        dp[r][c]+=dfs(nr,nc,er,ec)

    return dp[r][c]

N,M,O=map(int,sys.stdin.readline().split())
board=[[0 for _ in range(M)] for _ in range(N)]

tmp=1
for i in range(N):
    for j in range(M):
        board[i][j]=tmp
        tmp+=1

dp=[[-1 for _ in range(M)] for _ in range(N)]
if O==0:
    print(dfs(0,0,N-1,M-1))
else:
    o_r,o_c=0,0
    for i in range(N):
        for j in range(M):
            if board[i][j]==O:
                o_r,o_c=i,j
    print(dfs(0,0,o_r,o_c)*dfs(o_r,o_c,N-1,M-1))