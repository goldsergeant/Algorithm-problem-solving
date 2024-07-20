import collections
import sys

T = int(sys.stdin.readline())
answer=[]
for _ in range(T):
    H, W, O, F, S_X, S_Y, E_X, E_Y = map(int, sys.stdin.readline().split())
    board = [[0 for _ in range(W + 1)] for _ in range(H + 1)]
    visited=[[-sys.maxsize for _ in range(W + 1)] for _ in range(H + 1)]
    for _ in range(O):
        x, y, l = map(int, sys.stdin.readline().split())
        board[x][y] = l

    visited[S_X][S_Y] = F
    q=collections.deque([(S_X, S_Y, F)])
    while q:
        x,y,f=q.popleft()
        if x==E_X and y==E_Y:
            break

        for dx,dy in (0,-1),(0,1),(-1,0),(1,0),:
            nx,ny=x+dx,y+dy
            if nx<=0 or nx>H or ny<=0 or ny>W:
                continue
            if board[nx][ny]-board[x][y]<=f and f-1>visited[nx][ny] and f>0:
                q.append((nx,ny,f-1))
                visited[nx][ny]=f-1

    answer.append('잘했어!!' if visited[E_X][E_Y]!=-sys.maxsize else '인성 문제있어??')

print(*answer, sep='\n')