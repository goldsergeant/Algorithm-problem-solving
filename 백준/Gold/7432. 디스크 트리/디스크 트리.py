import collections
import sys
sys.setrecursionlimit(100000)

N=int(sys.stdin.readline())
tree=collections.defaultdict(set)
for _ in range(N):
    nodes=['root']+sys.stdin.readline().rstrip().split('\\')
    path='root'
    for i in range(1,len(nodes)):
        tree[path].add(f'{path}:{nodes[i]}')
        path+=f':{nodes[i]}'

for key,s in tree.items():
    tree[key]=sorted(s)
def dfs(node,depth):
    if depth!=-1:
        print(' '*depth+node.split(':')[-1])
    for next_node in tree[node]:
        dfs(next_node,depth+1)

dfs('root',-1)
