import collections
import sys
sys.setrecursionlimit(100000)

T=int(sys.stdin.readline())

def dfs(node,depth):
    level[node]=depth
    for next_node in tree[node]:
        dfs(next_node,depth+1)

for _ in range(T):
    N=int(sys.stdin.readline())
    tree=collections.defaultdict(list)
    reverse_tree=collections.defaultdict(int)
    level=[0 for _ in range(N+1)]
    for _ in range(N-1):
        A,B=map(int,sys.stdin.readline().split())
        tree[A].append(B)
        reverse_tree[B]=A

    a,b=map(int,sys.stdin.readline().split())

    root=0
    for i in range(1,N+1):
        if not reverse_tree[i]:
            root=i
            break

    dfs(root,0)

    while level[a]<level[b]:
        b=reverse_tree[b]
    while level[a]>level[b]:
        a=reverse_tree[a]

    while a!=b:
        a=reverse_tree[a]
        b=reverse_tree[b]

    print(a)