n,m=map(int,input().split())
k=int(input())
dy=[1,0]
dx=[0,1]

construct_roads=[]
dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
dp[0][0]=1
for _ in range(k):
    a,b,c,d=map(int,input().split())
    construct_roads.append((a,b,c,d))

dp[0][0]=1
for i in range(m+1):
    for j in range(n+1):
        for idx in range(2):
            ny=i+dy[idx]
            nx=j+dx[idx]
            if ny>m or nx>n: #좌표 벗어나면 볼필요없음
                continue
            flag=0
            for construct_road in construct_roads:
                a,b,c,d=construct_road
                if (b==i and a==j and d==ny and c==nx) or (d==i and c==j and b==ny and a==nx):
                    flag=1
                    break
            if flag==1:
                continue

            dp[ny][nx]+=dp[i][j]

print(dp[-1][-1])