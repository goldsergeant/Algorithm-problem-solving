import sys
sys.setrecursionlimit(10000)

n, m, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
parent = [i for i in range(n + 1)]
visited = [False for _ in range(n + 1)]
answer=0


def find(x):
    if x == parent[x]:
        return x
    return find(parent[x])

def union(first,second):
    first=find(first)
    second=find(second)
    if first!=second:
        if a[first]<a[second]:
            parent[second]=first
        else:
            parent[first]=second


for _ in range(m):
    first, second = map(int, sys.stdin.readline().split())
    union(first,second)

for i in range(1, n + 1):
    root=find(i)
    if not visited[root]:
        if k >= a[root]:
            k -= a[root]
            answer+=a[root]
            visited[root] = True
            union(root,i)
        else:
            print('Oh no')
            exit()

print(answer)