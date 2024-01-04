import collections
import sys

N,M,K=map(int,sys.stdin.readline().split())
nourish=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
board=[[5 for _ in range(N)] for _ in range(N)]
tree=[[collections.deque() for _ in range(N)] for _ in range(N)]
dead_trees=[]
for _ in range(M):
    y,x,z=map(int,sys.stdin.readline().split())
    tree[y-1][x-1].append(z)

def spring():
    for i in range(N):
        for j in range(N):
            tmp_len=len(tree[i][j])
            for k in range(tmp_len):
                if board[i][j]<tree[i][j][k]:
                    for _ in range(k,tmp_len):
                        dead_trees.append((i,j,tree[i][j].pop()))
                    break
                else:
                    board[i][j]-=tree[i][j][k]
                    tree[i][j][k]+=1

def summer():
    while dead_trees:
        y,x,z=dead_trees.pop()
        board[y][x]+=(z//2)

def autumn():
    for y in range(N):
        for x in range(N):
            tmp_len=len(tree[y][x])
            for k in range(tmp_len):
                if tree[y][x][k]%5==0:
                    for n_r,n_c in [(y-1, x-1), (y-1, x), (y-1, x+1), (y, x-1), (y, x+1), (y+1, x-1), (y+1, x), (y+1, x+1)]:
                        if 0<=n_r<N and 0<=n_c<N:
                            tree[n_r][n_c].appendleft(1)

def winter():
    for i in range(N):
        for j in range(N):
            board[i][j]+=nourish[i][j]

for _ in range(K):
    spring()
    summer()
    autumn()
    winter()

answer=0
for i in range(N):
    for j in range(N):
        answer+=len(tree[i][j])

print(answer)