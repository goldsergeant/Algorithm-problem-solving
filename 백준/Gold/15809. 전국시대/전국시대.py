import sys


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]=a
        army[a]+=army[b]
        army[b]=0
    else:
        parent[a]=b
        army[b]+=army[a]
        army[a]=0

def fight(a,b):
    a=find(a)
    b=find(b)
    if army[a]>army[b]:
        parent[b]=a
        army[a]-=army[b]
        army[b]=0
    elif army[a]<army[b]:
        parent[a]=b
        army[b]-=army[a]
        army[a]=0
    else:
        parent[a]=0
        parent[b]=0
        army[a]=0
        army[b]=0


N, M = map(int, sys.stdin.readline().split())
army = [0] + list(int(sys.stdin.readline()) for _ in range(N))
parent = [i for i in range(N + 1)]
for _ in range(M):
    opt, p, q = map(int, sys.stdin.readline().split())
    if opt == 1:
        union(p,q)
    else:
        fight(p,q)

visited=[False for _ in range(N+1)]
answer=[]
for i in range(1,N+1):
    p=find(i)
    if not visited[p] and p!=0:
        answer.append(army[p])
        visited[p]=True

print(len(answer))
if answer:
    print(*sorted(answer))