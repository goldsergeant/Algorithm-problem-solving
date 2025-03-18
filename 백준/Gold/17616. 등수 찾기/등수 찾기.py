import collections
import sys

N,M,X=map(int,sys.stdin.readline().split())
graph1=collections.defaultdict(list)
graph2=collections.defaultdict(list)
in_degree1=[0 for _ in range(N+1)]
in_degree2=[0 for _ in range(N+1)]
rank1=[0 for _ in range(N+1)]
rank2=[0 for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph1[b].append(a)
    in_degree1[a]+=1

    graph2[a].append(b)
    in_degree2[b]+=1

q1=collections.deque()
q2=collections.deque()
for i in range(1,N+1):
    if in_degree1[i]==0:
        q1.append(i)
    if in_degree2[i]==0:
        q2.append(i)

cur_rank=N
while q1:
    for _ in range(len(q1)):
        node=q1.popleft()
        rank1[node]=cur_rank
        for next_node in graph1[node]:
            in_degree1[next_node]-=1
            if in_degree1[next_node]==0:
                q1.append(next_node)

        cur_rank-=1

cur_rank=1
while q2:
    for _ in range(len(q2)):
        node=q2.popleft()
        rank2[node]=cur_rank
        for next_node in graph2[node]:
            in_degree2[next_node]-=1
            if in_degree2[next_node]==0:
                q2.append(next_node)

        cur_rank+=1

print(rank2[X],rank1[X])