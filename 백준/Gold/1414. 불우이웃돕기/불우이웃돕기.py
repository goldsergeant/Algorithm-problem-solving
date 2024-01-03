import collections
import sys
from heapq import heappush,heappop

N=int(sys.stdin.readline())
graph=collections.defaultdict(list)
arr=[]
total_lan=0

for _ in range(N):
    tmp=list(sys.stdin.readline().rstrip())
    for i in range(len(tmp)):
        if tmp[i].isupper():
            tmp[i]=ord(tmp[i])-38
        elif tmp[i].islower():
            tmp[i]=ord(tmp[i])-96
        else:
            tmp[i]=0
    total_lan+=sum(tmp)
    arr.append(tmp)


for i in range(N):
    for j in range(N):
        if arr[i][j]!=0:
            graph[i+1].append((j+1,arr[i][j]))
            graph[j+1].append((i+1,arr[i][j]))

def prim():
    visited=[False]*(N+1)
    total_weight=0
    q=[(0,1)]
    while q:
        distance,node=heappop(q)
        if not visited[node]:
            visited[node]=True
            total_weight+=distance

            for next_node,next_distance in graph[node]:
                if not visited[next_node]:
                    heappush(q,(next_distance,next_node))

    return total_weight if all(visited[1:]) else -1

spanning_weight=prim()
print(total_lan - spanning_weight if spanning_weight!=-1 else -1)