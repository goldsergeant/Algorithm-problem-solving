import sys

n,m=map(int,input().split())
a=[]
move_info=[]
cloud=[[n-1,0],[n-1,1],[n-2,0],[n-2,1]]
directions=[(0,0),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

dy=[-1,-1,1,1]
dx=[-1,1,-1,1]

for _ in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))

for _ in range(m):
    num,distance=map(int,sys.stdin.readline().split())
    move_info.append((num,distance))

for i in range(len(move_info)):
    num,distance=move_info[i]
    visited=[[False for _ in range(n)] for _ in range(n)]

    for i in range(len(cloud)): # 1번
        cloud[i][0]+=directions[num][0]*distance
        cloud[i][1]+=directions[num][1]*distance
        if cloud[i][0]>n-1:
            cloud[i][0]%=n
        elif cloud[i][0]<0:
            while cloud[i][0]<0:
                cloud[i][0]=n+cloud[i][0]
        if cloud[i][1]>n-1:
            cloud[i][1]%=n
        elif cloud[i][1]<0:
            while cloud[i][1]<0:
                cloud[i][1]=n+cloud[i][1]

    for i in range(len(cloud)): # 2번
        r,c=cloud[i]
        a[r][c]+=1

    for i in range(len(cloud)): # 4번
        r,c=cloud[i]
        water_cnt=0
        for j in range(4):
            nr=r+dy[j]
            nc=c+dx[j]
            if nr<0 or nr>n-1 or nc<0 or nc>n-1:
                continue
            if a[nr][nc]>0:
                water_cnt+=1
        a[r][c]+=water_cnt

    for i in range(len(cloud)):
        r,c=cloud[i]
        visited[r][c]=True

    cloud.clear() # 3번

    for i in range(n): # 5번
        for j in range(n):
            if not visited[i][j]:
                if a[i][j]>=2:
                    cloud.append([i,j])
                    a[i][j]-=2

print(sum(sum(a[i]) for i in range(n)))
