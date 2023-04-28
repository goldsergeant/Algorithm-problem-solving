import collections

S = int(input())


def bfs():
    queue = collections.deque()
    queue.append((1, 0, 0))
    visited = [[False for _ in range(1001)] for _ in range(1001)]

    while queue:
        temp = queue.popleft()
        screen, depth, clipboard = temp[0], temp[1], temp[2]
        visited[0][0] = True
        if screen == S:
            return depth

        if not visited[screen][screen]:  # 1번 연산
            visited[screen][screen] = True
            queue.append((screen, depth + 1, screen))

        if screen + clipboard < 1001 and clipboard>0 and not visited[screen + clipboard][screen]:  # 2번 연산
            visited[screen + clipboard][screen] = True
            queue.append((screen + clipboard, depth + 1, clipboard))

        if screen > 0 and not visited[screen - 1][screen]:  # 3번 연산
            visited[screen - 1][screen] = True
            queue.append((screen - 1, depth + 1, clipboard))


print(bfs())
