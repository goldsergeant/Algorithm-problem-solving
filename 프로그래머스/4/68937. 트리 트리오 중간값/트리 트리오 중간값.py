import collections
import sys
from heapq import heappop,heappush

def solution(n, edges):
    graph=collections.defaultdict(list)
    answer=0
    def get_farthest_node(start):
        visited=[False for _ in range(n+1)]
        visited[start]=True
        q=collections.deque([(start,0)])
        longest=0
        farthest_node=0

        while q:
            node,dist=q.popleft()
            if dist>longest:
                longest=dist
                farthest_node=node

            for adj in graph[node]:
                if not visited[adj]:
                    visited[adj]=True
                    q.append((adj,dist+1))

        return farthest_node,longest

    def get_distance(start):
        distance=[sys.maxsize for _ in range(n+1)]
        distance[start]=0
        q=collections.deque([(start,0)])
        while q:
            node,dist=q.popleft()
            for adj in graph[node]:
                if distance[adj]>dist+1:
                    distance[adj]=dist+1
                    q.append((adj,dist+1))

        return distance

    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)



    farthest1,longest1=get_farthest_node(1)
    farthest2,longest2=get_farthest_node(farthest1)
    distance1=get_distance(farthest1)
    distance2=get_distance(farthest2)

    for i in range(1,n+1):
        if i==farthest1 or i==farthest2:
            continue

        answer=max(answer,sorted([longest2,distance1[i],distance2[i]])[1])
    return answer

