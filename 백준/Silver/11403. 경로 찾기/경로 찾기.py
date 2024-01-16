import collections
import sys

N=int(sys.stdin.readline())
graph=[[]]
for i in range(1,N+1):
    roads=[0]+list(map(int,sys.stdin.readline().split()))
    graph.append(roads)

def bfs(start):
    q=collections.deque([start])
    visited=[False]*(N+1)
    answer=graph[start].copy()
    while q:
        cur=q.popleft()
        for i in range(1,N+1):
            if not visited[i] and graph[cur][i]==1:
                visited[i]=True
                answer[i]=1
                q.append(i)


    return answer[1:]

for i in range(1,N+1):
    print(*bfs(i))