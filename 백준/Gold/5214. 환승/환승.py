import collections
import itertools
import sys

N,K,M=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
for i in range(M):
    stations=list(map(int,sys.stdin.readline().split()))
    for j in range(len(stations)):
        graph[stations[j]].append(N+i+1)
        graph[N+i+1].append(stations[j])

def bfs():
    q=collections.deque([(1,1)])
    visited=[sys.maxsize]*(N+M+1)
    visited[1]=1
    possible_dists=[]

    while q:
        dist,node=q.popleft()
        if node==N:
            possible_dists.append(dist)
            continue

        for next_node in graph[node]:
            if node>N:
                if dist<visited[next_node]:
                    visited[next_node]=dist
                    q.append((dist,next_node))
            else:
                if dist+1<visited[next_node]:
                    visited[next_node]=dist+1
                    q.append((dist+1,next_node))

    return min(possible_dists) if possible_dists else -1
print(bfs())