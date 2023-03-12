import collections
import heapq
import sys

def dijkstra(start,end):
    distance=[sys.maxsize for i in range(n+1)]
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist:
            continue

        for i in graph[now]:
            cost=dist+i[1]

            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(q,(distance[i[0]],i[0]))
    return distance[end]

n,e=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
for _ in range(e):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
v1,v2=map(int,sys.stdin.readline().split())

path1=dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,n)
path2=dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,n)
answer=min(path2,path1)
print(answer if answer<sys.maxsize else -1 )



