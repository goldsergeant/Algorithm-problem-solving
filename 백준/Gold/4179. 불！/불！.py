import collections
import sys

R,C=map(int,sys.stdin.readline().split())
board=[list(sys.stdin.readline().strip()) for _ in range(R)]
fire_board=[[sys.maxsize for _ in range(C)] for _ in range(R)]
jihoon_board=[[sys.maxsize for _ in range(C)] for _ in range(R)]
j_s,j_c=0,0
q=collections.deque()
for i in range(R):
    for j in range(C):
        if board[i][j]=='F':
            q.append((i,j))
            fire_board[i][j]=0
        elif board[i][j]=='J':
            j_s,j_c=i,j
            jihoon_board[i][j]=0


while q:
    r,c=q.popleft()
    for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
        nr,nc=r+dr,c+dc
        if 0<=nr<R and 0<=nc<C:
            if board[nr][nc]!='#' and fire_board[nr][nc]>fire_board[r][c]+1:
                fire_board[nr][nc]=fire_board[r][c]+1
                q.append((nr,nc))


q=collections.deque([(j_s,j_c)])
while q:
    r,c=q.popleft()
    for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
        nr,nc=r+dr,c+dc
        if 0<=nr<R and 0<=nc<C:
            if board[nr][nc]!='#' and jihoon_board[nr][nc]>jihoon_board[r][c]+1 and fire_board[nr][nc]>jihoon_board[r][c]+1:
                jihoon_board[nr][nc]=jihoon_board[r][c]+1
                q.append((nr,nc))
        else:
            print(jihoon_board[r][c]+1)
            exit()

print('IMPOSSIBLE')