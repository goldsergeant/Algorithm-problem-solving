import sys

n,m=map(int,sys.stdin.readline().split())
answer=1
visited=[[False for _ in range(m)] for _ in range(n)]
pos=[(-1,0),(-1,-1),(0,-1)]

def can_remove(row,col):
    if row>=1 and col>=1:
        flag = 0
        for k in range(3):
            n_i=row+pos[k][0]
            n_j=col+pos[k][1]
            if not visited[n_i][n_j]:
                flag=1
        if flag==0:
            return True
        return False
    return False
def dfs(row,col,depth):
    global answer
    answer+=1
    for i in range(row,n):
        for j in range(m):
            if i==row and j<=col:
                continue
            if not visited[i][j] and not can_remove(i,j):
                visited[i][j]=True
                dfs(i,j,depth+1)
                visited[i][j]=False

for i in range(n):
    for j in range(m):
        visited[i][j]=True
        dfs(i,j,1)
        visited[i][j]=False

print(answer)