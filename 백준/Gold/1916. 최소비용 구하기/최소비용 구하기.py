import collections
import heapq
import sys

n = int(input())
m = int(input())
costArr = [sys.maxsize] * (n+1)
costArr[0]=0
graph = collections.defaultdict(list)
for _ in range(m):
    start_num, end_num, cost = map(int, input().split())
    graph[start_num].append((end_num, cost))


def dijkstra(start):
    queue=[]
    heapq.heappush(queue,(0,start))
    costArr[start]=0
    while queue:
        distance,point=heapq.heappop(queue)
        if costArr[point]<distance:
            continue
        for node in graph[point]:
            if costArr[node[0]]>distance+node[1]:
                costArr[node[0]]=distance+node[1]
                heapq.heappush(queue,(distance+node[1],node[0]))

start,end=map(int,input().split())
dijkstra(start)
print(costArr[end])
