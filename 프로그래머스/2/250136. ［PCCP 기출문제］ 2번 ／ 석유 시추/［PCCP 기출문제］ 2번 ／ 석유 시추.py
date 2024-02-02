import collections

def solution(land):
    visited = [[False for _ in range(len(land[0]))] for _ in range(len(land))]
    cols_amount=[0 for _ in range(len(land[0]))]
    for i in range(len(land)):
        for j in range(len(land[i])):
            if not visited[i][j] and land[i][j]==1:
                bfs(i,j,land,visited,cols_amount)
    return max(cols_amount)

def bfs(s_row,s_col,land,visited,cols_amount):
    amount=0
    q=collections.deque([(s_row,s_col)])
    visited[s_row][s_col]=True
    cols=set()
    cols.add(s_col)
    
    while q:
        row,col=q.popleft()
        cols.add(col)
        amount+=land[row][col]
        for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            n_row=dy+row
            n_col=dx+col
            if 0<=n_row<len(land) and 0<=n_col<len(land[0]):
                if not visited[n_row][n_col] and land[n_row][n_col]==1:
                    visited[n_row][n_col]=True
                    q.append((n_row,n_col))
    for col in cols:
        cols_amount[col]+=amount