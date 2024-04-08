import sys
sys.setrecursionlimit(1000000)

N,M=map(int,sys.stdin.readline().split())
board=[list(sys.stdin.readline().rstrip()) for _ in range(N)]
dp=[[-1 for _ in range(M)] for _ in range(N)]
answer=0

def get_next_point(r,c):
    if board[r][c]=='U':
        return r-1,c
    if board[r][c]=='R':
        return r,c+1
    if board[r][c]=='D':
        return r+1,c
    if board[r][c]=='L':
        return r,c-1

def dfs(r,c):
    if r<0 or r>=N or c<0 or c>=M:
        return 1
    if dp[r][c]!=-1:
        return dp[r][c]
    dp[r][c]=0
    n_r,n_c=get_next_point(r,c)

    dp[r][c]=dfs(n_r,n_c)
    return dp[r][c]

for i in range(N):
    for j in range(M):
        answer+=dfs(i,j)

print(answer)