import collections
import sys

N=int(input())
graph=collections.defaultdict(list)
visited=[-1 for _ in range(N+1)]
children = [set() for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

arr=list(map(int,sys.stdin.readline().split()))

def bfs():
    queue=collections.deque()
    queue.append((1,0))
    visited[1]=0

    while queue:
        u,depth=queue.popleft()
        for v in graph[u]:
            if visited[v]==-1:
                visited[v]=depth+1
                children[u].add(v)
                queue.append((v,depth+1))

bfs()
counter=collections.Counter(visited)

check_index=1
for i in arr:
    c_length=len(children[i])
    c1=set(arr[check_index:check_index + c_length])
    c2=children[i]
    if c1!=c2:
        print(0)
        exit()
    check_index+=c_length

print(1)