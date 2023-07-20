import copy
import itertools
import sys

n,m=map(int,input().split())
board=[]
dy=[-1,1,0,0]
dx=[0,0,-1,1]
zero_index=[]
answer=[]
virus=[]

for _ in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))

def dfs(row, col, clone_board):
    for i in range(4):
        ny=row+dy[i]
        nx=col+dx[i]
        if ny<0 or nx<0 or ny>n-1 or nx>m-1:
            continue
        if clone_board[ny][nx]==0:
            clone_board[ny][nx]=2
            dfs(ny, nx, clone_board)

for i in range(n):
    for j in range(m):
        if board[i][j]==0:
            zero_index.append((i,j))
        elif board[i][j]==2:
            virus.append((i,j))

for combi in itertools.combinations(zero_index,3):
    clone_board=copy.deepcopy(board)
    one=combi[0]
    two=combi[1]
    three=combi[2]
    clone_board[one[0]][one[1]]=1
    clone_board[two[0]][two[1]]=1
    clone_board[three[0]][three[1]]=1
    for v in virus:
        dfs(v[0],v[1],clone_board)
    answer.append(sum(i.count(0) for i in clone_board))

print(max(answer))
