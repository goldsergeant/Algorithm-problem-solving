import collections
import sys

N,M,fuel=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
t_r,t_c=map(lambda x:int(x)-1,sys.stdin.readline().split())
customer_targets=dict()
for _ in range(M):
    r1,c1,r2,c2=map(lambda x:int(x)-1,sys.stdin.readline().split())
    customer_targets[(r1,c1)]=(r2,c2)

def exit_game():
    print(-1)
    exit()
def get_shortest_customer(t_r,t_c):
    q=collections.deque([(0,t_r,t_c)])
    target_customers=[]
    visited=[[False for _ in range(N)] for _ in range(N)]
    visited[t_r][t_c]=True

    while q:
        for _ in range(len(q)):
            cnt,r,c=q.popleft()
            if (r,c) in customer_targets:
                target_customers.append((cnt,r,c))

            for dr,dc in (0,-1),(0,1),(-1,0),(1,0),:
                nr,nc=r+dr,c+dc
                if 0<=nr<N and 0<=nc<N:
                    if not visited[nr][nc] and board[nr][nc]==0:
                        visited[nr][nc]=True
                        q.append((cnt+1,nr,nc))
        if target_customers:
            break
    if not target_customers:
        exit_game()
    return sorted(target_customers)[0]

def get_dist_from_to(f_r,f_c,t_r,t_c):
    visited=[[False for _ in range(N)] for _ in range(N)]
    visited[f_r][f_c]=True
    q=collections.deque([(0,f_r,f_c)])
    while q:
        cnt,r,c=q.popleft()
        if (r,c)==(t_r,t_c):
            return cnt
        for dr,dc in (0,-1),(0,1),(-1,0),(1,0),:
            nr,nc=r+dr,c+dc
            if 0<=nr<N and 0<=nc<N:
                if not visited[nr][nc] and board[nr][nc]==0:
                    visited[nr][nc]=True
                    q.append((cnt+1,nr,nc))

    return sys.maxsize


for _ in range(M):
    c_cnt,c_r,c_c=get_shortest_customer(t_r,t_c)
    if c_cnt>fuel:
        exit_game()
    fuel-=c_cnt
    target_r,target_c=customer_targets[(c_r,c_c)]
    target_dist=get_dist_from_to(c_r,c_c,target_r,target_c)
    if target_dist>fuel:
        exit_game()

    customer_targets.pop((c_r,c_c))
    fuel-=target_dist
    fuel+=target_dist*2
    t_r,t_c=target_r,target_c

print(fuel)