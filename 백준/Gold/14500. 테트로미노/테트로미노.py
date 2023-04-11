import sys

n,m=map(int,sys.stdin.readline().split())
papers=[]
x_move=[1, -1, 0, 0]
y_move=[0, 0, 1, -1]
answer=[]
visited=[[False for _ in range(m)] for _ in range(n)]
def dfs(x,y,depth,sum_num):
    if depth==4:
        answer.append(sum_num)
        return
    for i in range(4):
        nx= x + x_move[i]
        ny= y + y_move[i]
        if 0<=nx<m and 0<=ny<n and not visited[ny][nx]:
            visited[ny][nx]=True
            dfs(nx,ny,depth+1,sum_num+papers[ny][nx])
            visited[ny][nx]=False

def not_dfs(x,y):
    for i in range(4):
        temp = papers[y][x]
        for k in range(3):
            t = (i+k)%4
            nx=x+x_move[t]
            ny=y+y_move[t]
            if nx<0 or nx>m-1 or ny<0 or ny>n-1:
                temp=0
                break
            temp+=papers[ny][nx]
        answer.append(temp)
for _ in range(n):
    papers.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        visited[i][j]=True
        dfs(j,i,1,papers[i][j])
        visited[i][j]=False
        not_dfs(j,i)

print(max(answer))
