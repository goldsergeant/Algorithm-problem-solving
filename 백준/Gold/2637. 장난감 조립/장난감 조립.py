import collections
import sys

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
graph=collections.defaultdict(list)
indegree=[0 for _ in range(N+1)]
outdegree=[0 for _ in range(N+1)]
cnt_degree=[0 for _ in range(N+1)]
for _ in range(M):
    x,y,z=map(int,sys.stdin.readline().split())
    graph[x].append((y,z))
    indegree[y]+=1
    outdegree[x]+=1

q=collections.deque()
for i in range(1,N+1):
    if indegree[i]==0 and outdegree[i]>0:
        q.append(i)
        cnt_degree[i]+=1

answer=collections.defaultdict(int)
while q:
    node=q.popleft()
    if outdegree[node]==0:
        answer[node]+=cnt_degree[node]
        continue

    for next_node,next_cnt in graph[node]:
        indegree[next_node]-=1
        cnt_degree[next_node]+=cnt_degree[node]*next_cnt
        if indegree[next_node]==0:
            q.append(next_node)

for key,val in sorted(answer.items()):
    print(key,val)