import collections
from heapq import heappush,heappop
import sys
            
def solution(n, paths, gates, summits):
    answer = [sys.maxsize,sys.maxsize]
    graph=[[] for _ in range(n+1)]
    distance=[sys.maxsize for _ in range(n+1)]
    is_summit=[False for _ in range(n+1)]
    for summit in summits:
        is_summit[summit]=True
        
    heap=[]
    for u,v,c in paths:
        graph[u].append((v,c))
        graph[v].append((u,c))
        
    for gate in gates:
        heappush(heap,(0,0,gate))
        distance[gate]=0
    
    while heap:
        cost,max_intensity,node=heappop(heap)
        max_intensity=max(max_intensity,cost)
        if max_intensity>distance[node]:
            continue
        if is_summit[node]:
            if max_intensity<answer[1] or (max_intensity==answer[1] and node<answer[0]):
                answer=[node,max_intensity]
            continue
            
        for next_node,next_cost in graph[node]:
            if max(next_cost,max_intensity)<distance[next_node]:
                distance[next_node]=max(next_cost,max_intensity)
                heappush(heap,(next_cost,max_intensity,next_node))
                
    return answer