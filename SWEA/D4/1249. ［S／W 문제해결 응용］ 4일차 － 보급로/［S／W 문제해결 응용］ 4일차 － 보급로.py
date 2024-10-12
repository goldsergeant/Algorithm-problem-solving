from heapq import heappush,heappop

def dijkstra():
    heap=[]
    heappush(heap,(0,0,0))
    distance=[[float('inf') for _ in range(N)] for _ in range(N)]
    distance[0][0]=0

    while heap:
        cost,r,c=heappop(heap)
        if cost>distance[r][c]:
            continue
        if r==N-1 and c==N-1:
            return distance

        for dy,dx in (-1,0),(1,0),(0,-1),(0,1):
            nr,nc=r+dy,c+dx
            if 0<=nr<N and 0<=nc<N:
                if cost+board[nr][nc]<distance[nr][nc]:
                    distance[nr][nc]=cost+board[nr][nc]
                    heappush(heap,(cost+board[nr][nc],nr,nc))


T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    board=[]
    for _ in range(N):
        arr=list(input())
        board.append(list(map(int,arr)))

    print(f'#{test_case} {dijkstra()[N-1][N-1]}')