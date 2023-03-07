import collections
import sys

t=int(input())
moves=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
for _ in range(t):
    l=int(input())
    cur_point=list(map(int,sys.stdin.readline().split()))
    dest_point=list(map(int,sys.stdin.readline().split()))
    board=[[0 for i in range(l)] for i in range(l)]
    queue=collections.deque()
    queue.append(cur_point+[0])
    while queue:
        y,x,count=queue.popleft()
        if y==dest_point[0] and x==dest_point[1]:
            print(count)
            break
        for move in moves:
            ny=y+move[0]
            nx=x+move[1]
            if ny<0 or ny>l-1 or nx<0 or nx>l-1 or board[ny][nx]==1:
                continue
            queue.append([ny,nx,count+1])
            board[ny][nx]=1
