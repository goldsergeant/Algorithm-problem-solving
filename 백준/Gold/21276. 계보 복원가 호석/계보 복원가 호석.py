import sys
import collections
sys.setrecursionlimit(10000)


def make_tree(node,depth):

    for next_node in graph[node]:
        if indegree[next_node]==depth+1:
            make_tree(next_node,depth+1)
            tree[node].append(next_node)
            tree_indegree[next_node]+=1
def dfs(node):
    children_cnt=len(tree[node])
    children=[]

    for child in sorted(tree[node]):
        children.append(child)
        dfs(child)

    node_info[node]=(children_cnt,*children)

N=int(sys.stdin.readline())
people=list(sys.stdin.readline().split())
M=int(sys.stdin.readline())
graph=collections.defaultdict(list)
tree=collections.defaultdict(list)
indegree=collections.defaultdict(int)
tree_indegree=collections.defaultdict(int)
for _ in range(M):
    x,y=sys.stdin.readline().split()
    graph[y].append(x)
    indegree[x]+=1

for name in people:
    if indegree[name]==0:
        make_tree(name,0)

root_nodes=set()
node_info=dict()

for name in people:
    if tree_indegree[name]==0:
        root_nodes.add(name)

for name in root_nodes:
    dfs(name)

print(len(root_nodes))
print(*sorted(root_nodes))
for name in sorted(people):
    print(name,*node_info[name])