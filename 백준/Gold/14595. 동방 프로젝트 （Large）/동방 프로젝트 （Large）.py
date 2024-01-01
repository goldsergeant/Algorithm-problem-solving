import collections
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parent = [i for i in range(N + 1)]
answer=0
visited=[False]*(N+1)
behaviors=[]
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b


for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    behaviors.append((x,y))

behaviors.sort()

last_room=0
for i in range(len(behaviors)):
    s,e=behaviors[i]
    s=max(s,last_room)
    for j in range(s,e+1):
        union(s,j)
    last_room=max(last_room,e)

for i in range(1,N+1):
    p=find(i)
    if not visited[p]:
        answer+=1
        visited[p]=True

print(answer)