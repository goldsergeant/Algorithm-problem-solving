def dfs(r,c):
    if dp[r][c]!=-1:
        return dp[r][c]

    dp[r][c]=1
    for dr,dc in (0,-1),(0,1),(1,0),(-1,0),:
        nr,nc=r+dr,c+dc
        if 0<=nr<N and 0<=nc<N and board[nr][nc]==board[r][c]+1:
            dp[r][c]=dfs(nr,nc)+1
            break
    return dp[r][c]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board=[list(map(int,input().split())) for _ in range(N)]
    dp=[[-1 for _ in range(N)] for _ in range(N)]
    answer_node=float('inf')
    answer_cnt=0
    for i in range(N):
        for j in range(N):
            if dp[i][j]==-1:
                if dfs(i,j)> answer_cnt:
                    answer_cnt=dfs(i,j)
                    answer_node=board[i][j]
                elif dfs(i,j)==answer_cnt:
                    answer_node=min(board[i][j],answer_node)

    print(f'#{test_case} {answer_node} {answer_cnt}')