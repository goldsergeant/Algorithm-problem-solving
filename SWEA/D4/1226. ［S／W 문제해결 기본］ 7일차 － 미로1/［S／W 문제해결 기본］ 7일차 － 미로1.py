def dfs(x,y):
    visited[x][y]=True
    if board[x][y]==3:
        return True

    tmp=False
    for dx,dy in (-1,0),(1,0),(0,-1),(0,1):
        nx,ny=x+dx,y+dy
        if 0<=nx<16 and 0<=ny<16:
            if not visited[nx][ny] and board[nx][ny]!=1:
                tmp=dfs(nx,ny)|tmp

    return tmp

for _ in range(1,10+1):
    test_case=int(input())
    board=[list(map(int,list(input()))) for _ in range(16)]
    visited=[[False for _ in range(16)] for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if board[i][j]==2:
                print(f'#{test_case} {int(dfs(i,j))}')