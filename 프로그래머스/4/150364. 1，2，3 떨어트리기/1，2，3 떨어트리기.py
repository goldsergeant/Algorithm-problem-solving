import collections
import sys

tree = collections.defaultdict(list)
route_points = []
answer = []
targets = None


def solution(edges, target):
    global route_points, targets
    targets = target
    target.insert(0, 0)
    route_points = [0 for _ in range(len(target) + 1)]
    counts = [0 for _ in range(len(target) + 1)]
    check = [False for _ in range(len(target) + 1)]
    remain_leaf_cnt = 0
    drop_order = []
    for parent, child in edges:
        tree[parent].append(child)

    for parent, children in tree.items():
        tree[parent].sort()

    for i in range(1, len(target)):
        if not tree[i] and target[i]>0:
            remain_leaf_cnt += 1

    while remain_leaf_cnt > 0:
        path = []
        get_path_to_leaf(path, 1)

        leaf_node = path[-1]
        counts[leaf_node] += 1
        drop_order.append(leaf_node)
        for node in path:
            if node != leaf_node:
                convert_next_route(node)

        if counts[leaf_node] > targets[leaf_node]:
            return [-1]

        if not check[leaf_node] and target[leaf_node] <= counts[leaf_node] * 3:
            remain_leaf_cnt -= 1
            check[leaf_node]=True

    for leaf_node in drop_order:
        counts[leaf_node]-=1
        for val in [1, 2, 3]:
            if counts[leaf_node]<=target[leaf_node]-val<=3*counts[leaf_node]:
                answer.append(val)
                target[leaf_node]-=val
                break
    return answer


def convert_next_route(node):
    route_points[node] = (route_points[node] + 1) % len(tree[node])


def get_path_to_leaf(path, node):
    path.append(node)
    if tree[node]:
        point = route_points[node]
        get_path_to_leaf(path, tree[node][point])



