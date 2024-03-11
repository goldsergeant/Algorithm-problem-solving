import sys

N,M=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp=[[sys.maxsize for _ in range(M)] for _ in range(N)]

def dfs(r,c):
    if r==N-1 and c==M-1:
        return 0
    if dp[r][c]!=sys.maxsize:
        return dp[r][c]

    v=sys.maxsize
    for d in range(1,board[r][c]+1):
        nr=r+d
        nc=c+d
        if nr<N:
            v=min(v,dfs(nr,c)+1)
        if nc<M:
            v=min(v,dfs(r,nc)+1)

    dp[r][c]=v
    return dp[r][c]

print(dfs(0,0))

