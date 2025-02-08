import collections
import sys
sys.setrecursionlimit(1000000)


def solution(nodeinfo):
    nodeinfo = [[0, 0, 0]] + nodeinfo
    pre_order_list = []
    post_order_list = []

    def make_tree(parent, child):
        parent_x = nodeinfo[parent][0]
        child_x = nodeinfo[child][0]
        if child_x < parent_x:
            if tree[parent][0] == -1:
                tree[parent][0] = child
            else:
                make_tree(tree[parent][0], child)
        else:
            if tree[parent][1] == -1:
                tree[parent][1] = child
            else:
                make_tree(tree[parent][1], child)

    def pre_order(node):
        pre_order_list.append(node)
        if tree[node][0] != -1:
            pre_order(tree[node][0])
        if tree[node][1] != -1:
            pre_order(tree[node][1])

    def post_order(node):
        if tree[node][0] != -1:
            post_order(tree[node][0])
        if tree[node][1] != -1:
            post_order(tree[node][1])
        post_order_list.append(node)

    tree = [[-1, -1] for _ in range(len(nodeinfo) + 1)]
    for i in range(1, len(nodeinfo)):
        nodeinfo[i].append(i)
    root = 0
    max_level = -sys.maxsize
    for i in range(1, len(nodeinfo)):
        if nodeinfo[i][1] > max_level:
            max_level = nodeinfo[i][1]
            root = i

    new_nodeinfo = [[0, 0, 0]] + sorted(nodeinfo[1:], key=lambda x: x[1], reverse=True)
    for i in range(2, len(new_nodeinfo)):
        make_tree(root, new_nodeinfo[i][2])

    pre_order(root)
    post_order(root)
    return [pre_order_list, post_order_list]


# print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
print(solution(([[0,0]])))