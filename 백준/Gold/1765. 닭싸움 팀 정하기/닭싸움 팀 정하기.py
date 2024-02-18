import collections
import sys

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
parent=[i for i in range(N+1)]
enemy_graph=collections.defaultdict(list)
answer=0

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def connect_enemy_of_enemy(start, node, depth, visited):
    visited[node]=True

    for next_node in enemy_graph[node]:
        if depth%2==0:
            union(start,next_node)
        if not visited[next_node]:
            connect_enemy_of_enemy(start, next_node, depth + 1, visited)

for _ in range(M):
    line=sys.stdin.readline().split()
    line[1:]=map(int,line[1:])
    a=line[1]
    b=line[2]
    if line[0]=='F':
        union(a,b)
    elif line[0]=='E':
        enemy_graph[a].append(b)
        enemy_graph[b].append(a)

for i in range(1,N+1):
    if enemy_graph[i]:
        visited=[False for _ in range(N+1)]
        connect_enemy_of_enemy(i, i, 1, visited)

visited=[False for _ in range(N+1)]
for i in range(N,0,-1):
    if not visited[find(i)]:
        visited[find(i)]=True
        answer+=1

print(answer)