import collections
import sys

DEPTH_PREFIX = '--'
N = int(sys.stdin.readline())
tree=collections.defaultdict(set)

for _ in range(N):
    arr = list(sys.stdin.readline().split())
    parent=0
    for i in range(1,len(arr)):
        tree[parent].add((arr[i],i-1,parent))
        parent=(arr[i],i-1,parent)

def dfs(node):
    value,floor,parent=node
    print(DEPTH_PREFIX * floor + value)
    for next_node in tree[node]:
        dfs(next_node)

for key in tree.keys():
    tree[key]=sorted(tree[key])

for node in tree[0]:
    dfs(node)

