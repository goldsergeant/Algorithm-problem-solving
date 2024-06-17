import collections
import sys

def find_customer():
    q=collections.deque([(taxi_r,taxi_c,0)])
    visited=[[False for _ in range(N)] for _ in range(N)]
    visited[taxi_r][taxi_c]=True
    target_customers=[]
    while q:
        r,c,dist=q.popleft()
        if board[r][c]==2:
            target_customers.append((r,c,dist))

        for dy,dx in [(-1,0),(0,1),(1,0),(0,-1)]:
            n_r,n_c=r+dy,c+dx
            if 0<=n_r<N and 0<=n_c<N:
                if not visited[n_r][n_c] and board[n_r][n_c]!=1:
                    visited[n_r][n_c]=True
                    q.append((n_r,n_c,dist+1))
    if not target_customers:
        print(-1)
        exit()
    return sorted(target_customers,key=lambda x:(x[2],x[0],x[1]))[0]
def get_shortest_dist(r,c,e_r,e_c):
    q=collections.deque([(0,r,c)])
    visited=[[False for _ in range(N)] for _ in range(N)]

    visited[r][c]=True
    while q:
        dist,row,col=q.popleft()
        if row==e_r and col==e_c:
            return dist

        for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            n_r,n_c=row+dy,col+dx
            if 0<=n_r<N and 0<=n_c<N:
                if not visited[n_r][n_c] and board[n_r][n_c]!=1:
                    visited[n_r][n_c]=True
                    q.append((dist+1,n_r,n_c))


N,M,FUEL=map(int,sys.stdin.readline().split())
board=[[*map(int,sys.stdin.readline().split())] for _ in range(N)]

customers=[]
taxi_r,taxi_c=map(lambda x:int(x)-1,sys.stdin.readline().split())

for _ in range(M):
    a,b,c,d=map(int,sys.stdin.readline().split())
    customers.append((a-1,b-1,c-1,d-1))
    board[a-1][b-1]=2

for _ in range(M):
    c_r,c_c,c_dist=find_customer()
    target_customer_idx=0
    target_customer=None
    for i in range(len(customers)):
        if customers[i][0]==c_r and customers[i][1]==c_c:
            target_customer=customers[i]
            target_customer_idx=i
            break

    to_customer_from_taxi=get_shortest_dist(taxi_r,taxi_c,target_customer[0],target_customer[1])
    if to_customer_from_taxi==None:
        print(-1)
        exit()
    if FUEL<to_customer_from_taxi:
        print(-1)
        exit()

    taxi_r,taxi_c=target_customer[0],target_customer[1]
    FUEL-=to_customer_from_taxi
    board[taxi_r][taxi_c]=0

    to_destination_from_taxi=get_shortest_dist(taxi_r,taxi_c,target_customer[2],target_customer[3])
    if to_destination_from_taxi==None:
        print(-1)
        exit()
    if FUEL<to_destination_from_taxi:
        print(-1)
        exit()

    taxi_r,taxi_c=target_customer[2],target_customer[3]
    FUEL-=to_destination_from_taxi
    FUEL+=to_destination_from_taxi*2

    customers.pop(target_customer_idx)

print(FUEL)