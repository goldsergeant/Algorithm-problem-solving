import collections
import sys

impossible_land = 0
possible_land = 1
target = 2

n, m = map(int, sys.stdin.readline().split())
board = []
target_idx=tuple()
dy=[-1,1,0,0]
dx=[0,0,-1,1]
for i in range(n):
    arr=list(map(int, sys.stdin.readline().split()))
    if 2 in arr:
        target_idx=(i,arr.index(2))
    board.append(arr)

def bfs():
    visited = [[-1] * m for _ in range(n)]
    queue=collections.deque()
    queue.append((target_idx[0],target_idx[1],0))
    visited[target_idx[0]][target_idx[1]]=0

    while queue:
        row,col,depth=queue.popleft()
        for i in range(4):
            n_row=row+dy[i]
            n_col=col+dx[i]

            if n_row<0 or n_col<0 or n_row>n-1 or n_col>m-1:
                continue


            if visited[n_row][n_col]==-1 and  board[n_row][n_col]==possible_land:
                visited[n_row][n_col]=depth+1
                queue.append((n_row,n_col,depth+1))


    return visited

visited=bfs()
for i in range(n):
    for j in range(m):
        if board[i][j]==impossible_land:
            print(impossible_land,end=' ')
        else:
            print(visited[i][j],end=' ')
    print()


