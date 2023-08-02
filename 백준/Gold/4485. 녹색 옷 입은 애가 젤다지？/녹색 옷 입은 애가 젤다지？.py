import heapq
import sys

input=sys.stdin.readline

dy=[0,0,1,-1]
dx=[1,-1,0,0]

def dijkstra(board):
    distance=[[sys.maxsize for _ in range(len(board))] for _ in range(len(board))]
    distance[0][0]=board[0][0]
    queue=[(distance[0][0],0,0)]
    while queue:
        cost,row,col=heapq.heappop(queue)
        if cost>distance[row][col]:
            continue
        for i in range(4):
            n_row=row+dy[i]
            n_col=col+dx[i]
            if n_row<0 or n_col<0 or n_row>len(board)-1 or n_col>len(board)-1:
                continue
            if cost+board[n_row][n_col]<distance[n_row][n_col]:
                distance[n_row][n_col]=cost+board[n_row][n_col]
                heapq.heappush(queue,(distance[n_row][n_col],n_row,n_col))

    return distance[-1][-1]



test_case=1
while True:
    n=int(input())
    if n==0:
        break

    board=[]
    for _ in range(n):
        board.append(list(map(int,input().split())))

    print(f'Problem {test_case}: {dijkstra(board)}')
    test_case+=1