import collections
import sys

n=int(sys.stdin.readline())
graph=collections.defaultdict(list)
cost=[0 for _ in range(n+1)]
indegree=[0 for _ in range(n+1)]
answer=[0 for _ in range(n+1)]


for i in range(1,n+1):
    line=list(map(int,sys.stdin.readline().split()))[:-1]
    cur_cost=line[0]
    cost[i]=cur_cost
    for j in range(1,len(line)):
        graph[line[j]].append(i)
        indegree[i]+=1

q=collections.deque()
for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)

while q:
    cur_node=q.popleft()
    answer[cur_node]+=cost[cur_node]

    for next_node in graph[cur_node]:
        answer[next_node]=max(answer[next_node],answer[cur_node])
        indegree[next_node]-=1
        if indegree[next_node]==0:
            q.append(next_node)


for n in answer[1:]:
    print(n)

