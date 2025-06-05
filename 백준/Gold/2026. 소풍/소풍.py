import collections
import sys

K,N,F=map(int,sys.stdin.readline().split())
connected=[[False for _ in range(N+1)] for _ in range(N+1)]
visited=[False for _ in range(N+1)]
friends_num=[0 for _ in range(N+1)]
for _ in range(F):
    a,b=map(int,sys.stdin.readline().split())
    connected[a][b]=True
    connected[b][a]=True
    friends_num[a]+=1
    friends_num[b]+=1

def dfs(node,friends):
    if len(friends)==K:
        print(*friends,sep='\n')
        exit()

    for i in range(1,N+1):
        if visited[i] or not connected[node][i]:
            continue
        if K-len(friends)>friends_num[i]:
            continue
        flag=True
        for f in friends:
            if not connected[i][f]:
                flag=False
                break
        if flag:
            visited[i]=True
            dfs(i,friends+[i])
            visited[i]=False

for i in range(1,N+1):
    if not visited[i]:
        visited[i]=True
        dfs(i,[i])

print(-1)