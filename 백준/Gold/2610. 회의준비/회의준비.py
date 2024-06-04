import collections
import pprint
import sys

def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b



N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
distance=[[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]
parent=[i for i in range(N+1)]
common_nodes=collections.defaultdict(list)
presidents=[]
set_cnt=0
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    distance[a][b]=1
    distance[b][a]=1
    union(a,b)
for i in range(1,N+1):
    distance[i][i]=0

for i in range(1,N+1):
    parent_node=find(i)
    if not common_nodes[parent_node]:
        set_cnt+=1
    common_nodes[parent_node].append(i)

print(set_cnt)
for key,nodes in common_nodes.items():
    for k in nodes:
        for i in nodes:
            for j in nodes:
                distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])

    answer_dist=sys.maxsize
    answer_node=0
    for cur_node in nodes:
        dist=0
        for next_node in nodes:
            if distance[cur_node][next_node]!=sys.maxsize and distance[cur_node][next_node]>dist:
                dist=distance[cur_node][next_node]
        if dist<answer_dist:
            answer_dist=dist
            answer_node=cur_node

    presidents.append(answer_node)

print(*sorted(presidents),sep='\n')