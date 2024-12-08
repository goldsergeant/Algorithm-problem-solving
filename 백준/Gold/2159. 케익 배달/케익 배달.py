import sys
dx=[0,-1,1,0,0]
dy=[0,0,0,-1,1]

def get_distance(x1,y1,x2,y2):
    return abs(x2-x1)+abs(y2-y1)

N=int(sys.stdin.readline())
init_x,init_y=map(int,sys.stdin.readline().split())
positions=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp=[[sys.maxsize for _ in range(5)] for _ in range(N)]

for i in range(5):
    dp[0][i]=get_distance(init_x,init_y,positions[0][0]+dx[i],positions[0][1]+dy[i])

for i in range(1,len(positions)):
    for j in range(5):
        for k in range(5):
            dp[i][j]=min(dp[i][j],dp[i-1][k]+get_distance(positions[i][0]+dx[j],positions[i][1]+dy[j],positions[i-1][0]+dx[k],positions[i-1][1]+dy[k]))

print(min(dp[-1]))