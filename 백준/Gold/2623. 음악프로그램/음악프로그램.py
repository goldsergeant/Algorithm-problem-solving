import collections
import sys

N,M=map(int,sys.stdin.readline().split())
parent=[[] for _ in range(N+1)]
in_degree=[0]*(N+1)
answer=[]
for _ in range(M):
    arr=list(map(int,sys.stdin.readline().split()))
    arr=arr[1:]
    for i in range(1,len(arr)):
        parent[arr[i]].append(arr[i-1])
        in_degree[arr[i-1]]+=1

q=collections.deque()
if 0 not in in_degree:
    print(0)
    exit()
for i in range(1,N+1):
    if in_degree[i]==0:
        q.append(i)

while q:
    node=q.popleft()
    answer.append(node)
    for parent_node in parent[node]:
        in_degree[parent_node]-=1
        if in_degree[parent_node]==0:
            q.appendleft(parent_node)

if len(answer)<N:
    print(0)
    exit()

for num in reversed(answer):
    print(num)
