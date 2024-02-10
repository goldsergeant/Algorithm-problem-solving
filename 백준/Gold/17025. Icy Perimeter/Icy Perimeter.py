import collections
import sys

VISITED='-'
ICECREAM='#'
EMPTY='.'

N=int(sys.stdin.readline())
board=[list(list(sys.stdin.readline().rstrip())) for _ in range(N)]
answer=[]
def bfs(r,c):
    q=collections.deque([(r,c,0)])
    board[r][c]=VISITED
    total_cnt=0
    total_perimeter=0

    while q:
        row,col,step=q.popleft()
        total_cnt+=1

        for dy,dx in [(1,0),(0,1),(-1,0),(0,-1)]:
            n_r,n_c=row+dy,col+dx
            if 0<=n_r<N and 0<=n_c<N: # 범위 안에 있다면
                if board[n_r][n_c]==ICECREAM:
                    board[n_r][n_c]=VISITED
                    q.append((n_r,n_c,step+1))

                elif board[n_r][n_c]==EMPTY:
                    total_perimeter+=1
            else: # 범위 바깥에 있다면
                total_perimeter+=1

    return total_cnt,total_perimeter


for i in range(N):
    for j in range(N):
        if board[i][j]=='#':
            answer.append(bfs(i,j))

print(*sorted(answer,key=lambda x:(x[0],-x[1]),reverse=True)[0])
