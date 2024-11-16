def dfs(r,c):
    visited[r][c]=True

    for dr,dc in (-1,0),(1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1):
        nr,nc=r+dr,c+dc
        if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
            if score[nr][nc]==0:
                dfs(nr,nc)
            elif score[nr][nc]>0:
                visited[nr][nc]=True

def make_score(r,c):
    cnt=0
    for dr,dc in (-1,0),(1,0),(0,-1),(0,1),(-1,1),(1,1),(1,-1),(-1,-1):
        nr,nc=r+dr,c+dc
        if 0<=nr<N and 0<=nc<N and board[nr][nc]=='*':
            cnt+=1

    score[r][c]=cnt


T= int(input())
for test_case in range(1,T+1):
    N=int(input())
    board=[list(input()) for _ in range(N)]
    score=[[-1 for _ in range(N)] for _ in range(N)]
    visited=[[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j]=='.':
                make_score(i,j)

    answer=0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if score[i][j]==0:
                    dfs(i,j)
                    answer+=1

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if score[i][j]>0 and not visited[i][j]:
                    answer+=1
                    visited[i][j]=True

    print(f'#{test_case} {answer}')