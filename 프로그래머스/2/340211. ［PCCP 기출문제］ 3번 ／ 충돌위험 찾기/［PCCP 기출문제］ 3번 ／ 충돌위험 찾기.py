import collections


def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def solution(points, routes):
    points.insert(0, [0, 0])
    unique_cnt_dict = collections.defaultdict(int)

    def bfs(s_node, route_idx):
        target_idx = 1
        s_x, s_y = points[s_node][0], points[s_node][1]
        q = collections.deque([(s_x, s_y, 0)])
        node = s_node
        while q:
            x, y, time = q.popleft()
            unique_cnt_dict[(x, y, time)] += 1
            target_node = routes[route_idx][target_idx]
            target_x,target_y=points[target_node][0],points[target_node][1]
            if (x, y) == (target_x, target_y):
                if target_idx == len(routes[route_idx]) - 1:
                    return
                target_idx += 1
                target_node = routes[route_idx][target_idx]

            target_x, target_y = points[target_node][0], points[target_node][1]

            distance = get_distance(x,y, target_x, target_y)
            next_x = 0
            next_y = 0
            for dx in [-1, 1]:
                nx = x + dx
                n_distance = get_distance(nx, y, target_x, target_y)
                if 1 <= nx <= 100:
                    if distance > n_distance:
                        next_x = nx
                        break

            for dy in [-1, 1]:
                ny = y + dy
                n_distance = get_distance(x, ny, target_x, target_y)
                if 1 <= ny <= 100:
                    if distance > n_distance:
                        next_y = ny
                        break

            if next_x != 0:
                q.append((next_x, y, time + 1))
            else:
                q.append((x, next_y, time + 1))

    answer = 0
    for i in range(len(routes)):
        s_node = routes[i][0]
        bfs(s_node, i)

    for key,val in unique_cnt_dict.items():
        if val>=2:
            answer+=1
    return answer


print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]]))
print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]]))
print(solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]]))
