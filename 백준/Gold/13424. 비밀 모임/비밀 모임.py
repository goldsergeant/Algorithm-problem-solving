import sys

T=int(sys.stdin.readline())
for _ in range(T):
    N,M=map(int,sys.stdin.readline().split())
    distance=[[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        a,b,c=map(int,sys.stdin.readline().split())
        distance[a][b]=c
        distance[b][a]=c
    for i in range(1,N+1):
        distance[i][i]=0
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])
    K=int(sys.stdin.readline())
    friend_rooms=list(map(int,sys.stdin.readline().split()))

    min_distance=sys.maxsize
    answer=0
    for i in range(1,N+1):
        total_distance=0
        for room in friend_rooms:
            total_distance+=distance[room][i]

        if total_distance<min_distance:
            min_distance=total_distance
            answer=i

    print(answer)