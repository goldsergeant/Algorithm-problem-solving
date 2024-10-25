def dfs(r,c,st):
    if len(st)==7:
        possibles.add(st)
        return
    for dy,dx in (-1,0),(1,0),(0,-1),(0,1),:
        ny,nx=r+dy,c+dx
        if 0<=ny<=3 and 0<=nx<=3:
            dfs(ny,nx,st+board[ny][nx])


T=int(input())
for test_case in range(1,T+1):
    board=[list(input().split()) for _ in range(4)]
    possibles=set()

    for i in range(4):
        for j in range(4):
            dfs(i,j,board[i][j])

    print(f'#{test_case} {len(possibles)}')