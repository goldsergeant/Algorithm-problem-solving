import collections
import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline
tree = collections.defaultdict(list)
graph = collections.defaultdict(list)
N, R = map(int, input().split())
GIGA = R
leaf_nodes = set()
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def make_tree(node):
    visited[node] = True
    for next_node, next_cost in graph[node]:
        if not visited[next_node]:
            tree[node].append((next_node, next_cost))
            make_tree(next_node)


def get_leaf_nodes(node):
    if not tree[node]:
        leaf_nodes.add(node)
    else:
        for next_node, next_cost in tree[node]:
            get_leaf_nodes(next_node)


def get_giga_nodes(node):
    if len(tree[node]) >= 2:
        return node

    for next_node, next_cost in tree[node]:
        return get_giga_nodes(next_node)


def get_branch_max_length(node):
    if node in leaf_nodes:
        return 0

    tmp = 0
    for next_node, next_cost in tree[node]:
        tmp = max(tmp, get_branch_max_length(next_node) + next_cost)

    return tmp


def get_pillar_length(node):
    if node == GIGA:
        return 0

    for next_node, next_cost in tree[node]:
        return next_cost + get_pillar_length(next_node)

visited=[False for _ in range(N+1)]
make_tree(R)
get_leaf_nodes(R)
if len(leaf_nodes) > 1:
    GIGA = get_giga_nodes(R)
else:
    GIGA = next(iter(leaf_nodes))

print(get_pillar_length(R), get_branch_max_length(GIGA))
