import collections
import sys
from itertools import combinations

N=int(sys.stdin.readline())
board=[list(sys.stdin.readline().split()) for _ in range(N)]
answer='NO'
teachers=[]

for i in range(N):
    for j in range(N):
        if board[i][j]=='T':
            teachers.append((i,j))

def check():
    for y,x in teachers:
        for dy,dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            n_y,n_x=y+dy,x+dx
            while 0<=n_y<N and 0<=n_x<N:
                if board[n_y][n_x]=='S':
                    return False
                elif board[n_y][n_x]=='T' or board[n_y][n_x]=='O':
                    break

                n_y+=dy
                n_x+=dx
    return True

for (y1,x1),(y2,x2),(y3,x3) in combinations([(i,j) for j in range(N) for i in range(N)],3):
    if board[y1][x1]=='X' and board[y2][x2]=='X' and board[y3][x3]=='X':
        board[y1][x1]='O'
        board[y2][x2]='O'
        board[y3][x3]='O'
        if check():
            answer='YES'
            break
        board[y1][x1]='X'
        board[y2][x2]='X'
        board[y3][x3]='X'

print(answer)
