import collections
import sys

dy=(-1,1,0,0,0,0)
dx=(0,0,-1,1,0,0)
dz=(0,0,0,0,-1,1)

def bfs(board):
    visited=[[[sys.maxsize for _ in range(C)] for _ in range(R)] for _ in range(L)]
    end=tuple()
    q=collections.deque()
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if board[i][j][k]=='S':
                    visited[i][j][k]=0
                    q.append((i,j,k))
                elif board[i][j][k]=='E':
                    end=(i,j,k)

    while q:
        floor,row,col=q.popleft()
        if (floor,row,col)==end:
            return f'Escaped in {visited[floor][row][col]} minute(s).'

        for i in range(6):
            n_floor,n_row,n_col=floor+dy[i],row+dz[i],col+dx[i]
            if 0<=n_floor<L and 0<=n_row<R and 0<=n_col<C:
                if visited[n_floor][n_row][n_col]>visited[floor][row][col]+1 and board[n_floor][n_row][n_col]!='#':
                    visited[n_floor][n_row][n_col]=visited[floor][row][col]+1
                    q.append((n_floor,n_row,n_col))

    return 'Trapped!'

while True:
    L, R, C = map(int, sys.stdin.readline().split())
    if L == R == C == 0:
        break
    board=[[] for _ in range(L)]
    for l in range(L):
        for _ in range(R):
            board[l].append(sys.stdin.readline().rstrip())
        sys.stdin.readline()

    print(bfs(board))