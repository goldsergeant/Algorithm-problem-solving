import collections
import sys

def bfs(idx):
    cnt=0
    q=collections.deque([idx])
    visited=[False for _ in range(N)]
    visited[idx]=True
    while q:
        i=q.popleft()
        cnt+=1
        for j in graph[i]:
            if not visited[j]:
                visited[j]=True
                q.append(j)

    return cnt


N=int(sys.stdin.readline())
cows=[[*map(int,sys.stdin.readline().split())] for _ in range(N)]
answer=0
graph=[[] for _ in range(N)]
for i in range(N):
    x1,y1,p1=cows[i]
    for j in range(i+1,N):
        x2,y2,p2=cows[j]
        distance=((x2-x1)**2+(y2-y1)**2)**(1/2)
        if distance<=p1:
            graph[i].append(j)
        if distance<=p2:
            graph[j].append(i)

for i in range(N):
    answer=max(answer,bfs(i))
print(answer)