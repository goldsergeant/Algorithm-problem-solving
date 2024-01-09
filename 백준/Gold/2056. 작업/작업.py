import collections
import sys

N=int(sys.stdin.readline())
graph=collections.defaultdict(list)
time=[0 for _ in range(N+1)]
answer=[0 for _ in range(N+1)]
indegree=[0 for _ in range(N+1)]
for i in range(1,N+1):
    arr=list(map(int,sys.stdin.readline().split()))
    t=arr[0]
    time[i]=t

    l=arr[1]
    if l!=0:
        pre_requires=arr[2:]
        for pre_require in pre_requires:
            graph[pre_require].append(i)
            indegree[i]+=1


stack=[]
for i in range(1,N+1):
    if indegree[i]==0:
        stack.append(i)
        indegree[i]=-1
        answer[i]=time[i]

while stack:
    node= stack.pop()
    for next_node in graph[node]:
        indegree[next_node]-=1
        answer[next_node]=max(answer[next_node],answer[node]+time[next_node])
        if indegree[next_node]==0:
            stack.append(next_node)
            indegree[next_node]=-1

print(max(answer))
