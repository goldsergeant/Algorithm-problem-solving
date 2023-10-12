import collections
import heapq
import sys
from math import sqrt

n=int(sys.stdin.readline())
point=dict()
graph=collections.defaultdict(list)
for i in range(1,n+1):
    x,y=map(float,sys.stdin.readline().split())
    point[i]=(x,y)

def calc_distance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

def prim(start):
    visited=[False]*(n+1)
    total_cost=0
    q=[]
    heapq.heappush(q,(0,start))

    while q:
        cur_cost,cur_node=heapq.heappop(q)
        if visited[cur_node]:
            continue
        visited[cur_node]=True
        total_cost+=cur_cost

        for next_distance,next_node in graph[cur_node]:
            if not visited[next_node]:
                heapq.heappush(q,(next_distance,next_node))

    return total_cost

for i in range(1,n+1):
    x1,y1=point[i]
    for j in range(i+1,n+1):
        x2,y2=point[j]
        graph[i].append((calc_distance(x1,y1,x2,y2),j))
        graph[j].append((calc_distance(x1,y1,x2,y2),i))

print(round(prim(1),2))