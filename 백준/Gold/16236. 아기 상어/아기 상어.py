import collections
import sys

def find_fishes(s_r,s_c,shark_size):
    visited=[[False for _ in range(N)] for _ in range(N)]
    visited[s_r][s_c]=True
    q=collections.deque([(s_r,s_c,0)])
    fishes=[] # r,c,거리
    while q:
        r,c,dist=q.popleft()

        for dy,dx in (-1,0),(0,-1),(1,0),(0,1):
            nr,nc=r+dy,c+dx
            if 0<=nr<N and 0<=nc<N:
                if not visited[nr][nc]:
                    if 0<board[nr][nc]<shark_size:
                        fishes.append((nr,nc,dist+1))
                    if board[nr][nc]<=shark_size:
                        visited[nr][nc]=True
                        q.append((nr,nc,dist+1))

    return fishes

def eat(s_r,s_c,f_r,f_c):
    global ate_cnt,shark_point
    ate_cnt+=1
    board[s_r][s_c],board[f_r][f_c]=0,board[s_r][s_c]
    shark_point=(f_r,f_c)


def upgrade():
    global shark_size,ate_cnt
    shark_size+=1
    ate_cnt=0



N=int(sys.stdin.readline())
board=[]
shark_point=None
shark_size=2
ate_cnt=0
time=0
for i in range(N):
    arr=list(map(int,sys.stdin.readline().split()))
    if 9 in arr:
        shark_point=(i, arr.index(9))
    board.append(arr)

while True:
    can_eat_fishes=find_fishes(shark_point[0],shark_point[1],shark_size)
    if not can_eat_fishes:
        break

    can_eat_fishes.sort(key=lambda x:(x[2],x[0],x[1]))

    decided_fish=can_eat_fishes[0]
    f_r,f_c=decided_fish[0],decided_fish[1]

    eat(shark_point[0],shark_point[1],f_r,f_c)
    time+=decided_fish[2]
    if ate_cnt==shark_size:
        upgrade()

print(time)