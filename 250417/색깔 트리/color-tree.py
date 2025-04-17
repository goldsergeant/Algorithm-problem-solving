import collections
import sys


def change_color(node, to_color):
    colors[node] = to_color
    for child in tree[node]:
        change_color(child, to_color)


def get_score(node):
    score = 0
    color_set = {colors[node]}
    for child in tree[node]:
        child_score, child_color_set = get_score(child)
        score += child_score
        color_set.update(child_color_set)
    score += (len(color_set)) ** 2
    return score, color_set


Q = int(input())
tree = collections.defaultdict(list)
max_depths = [sys.maxsize for _ in range(100000 + 1)]
colors = [-1 for _ in range(100000 + 1)]
for _ in range(Q):
    commands = list(map(int, input().split()))
    query = commands[0]
    if query == 100:  # 노드 추가
        m_id, p_id, color, max_depth = commands[1:]
        if p_id == -1:
            tree[p_id].append(m_id)
            max_depths[m_id] = max_depth
            colors[m_id] = color
        else:
            if max_depths[p_id] > 1:
                tree[p_id].append(m_id)
                max_depths[m_id] = min(max_depth, max_depths[p_id] - 1)
                colors[m_id] = color

    elif query == 200:  # 색깔 변경
        m_id, color = commands[1:]
        change_color(m_id, color)
    elif query == 300:  # 색깔 조회
        m_id = commands[1]
        print(colors[m_id])
    elif query == 400:  # 점수 조회
        score = 0
        for node in tree[-1]:
            score += get_score(node)[0]
        print(score)
