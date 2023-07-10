import sys

n,m=map(int,input().split())
cities=[]
houses=[]
chickens=[]
answer=[]
visited=[False for _ in range(13)]

def check(points):
    total=0
    for house in houses:
        tmp=sys.maxsize
        for point in points:
            tmp=min(tmp,abs(point[0]-house[0])+abs(point[1]-house[1]))
        total+=tmp
    return total
def dfs(start,points,depth):
    if depth==m:
        answer.append(check(points))
        return

    for i in range(start+1,len(chickens)):
        if not visited[i]:
            visited[i]=True
            dfs(i,points+[chickens[i]],depth+1)
            visited[i]=False


for _ in range(n):
    cities.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        if cities[i][j]==1:
            houses.append((i,j))
        elif cities[i][j]==2:
            chickens.append([i,j])


for i in range(len(chickens)):
    visited[i]=True
    dfs(i,[chickens[i]],1)
    visited[i]=False

print(sorted(answer)[0])