import collections
import sys

n,m,k=map(int,sys.stdin.readline().split())

board=[list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited=[[[False for _ in range(m)] for _ in range(n)] for _ in range(k+1)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
answer=[]

queue=collections.deque()
queue.appendleft((0,0,1,0)) # row,col,depth,break_count

while queue:
    row,col,depth,break_count= queue.pop()
    if row==n-1 and col==m-1:
        answer.append(depth)
        break

    for i in range(4):
        n_row=row+dy[i]
        n_col=col+dx[i]
        if n_row<0 or n_col<0 or n_row>n-1 or n_col> m-1:
            continue

        if not visited[break_count][n_row][n_col]:
            if board[n_row][n_col] == '0':
                visited[break_count][n_row][n_col]=True
                queue.appendleft((n_row,n_col,depth+1,break_count))
            else:
                if break_count<k and not visited[break_count+1][n_row][n_col]:
                    visited[break_count+1][n_row][n_col]=True
                    queue.appendleft((n_row,n_col,depth+1,break_count+1))

print(min(answer) if answer else -1)
